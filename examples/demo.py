"""Seeded vector-search example; optional adapter for NilVec 0.1.8's Python API."""

import argparse
import heapq
import json
import math
import random
import statistics
import time


def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def exact_search(vectors, query, k):
    """Return (Euclidean distance, insertion ID), with stable ID tie-breaking."""
    return heapq.nsmallest(
        k,
        ((math.dist(query, vector), i) for i, vector in enumerate(vectors)),
    )


def run(args):
    rng = random.Random(args.seed)
    vectors = [
        [rng.random() for _ in range(args.dimensions)]
        for _ in range(args.vectors)
    ]
    queries = [
        [rng.random() for _ in range(args.dimensions)]
        for _ in range(args.queries)
    ]
    k = min(args.k, len(vectors))
    index = None
    insertion_seconds = None
    if args.backend == "nilvec":
        try:
            import nilvec
        except ImportError as error:
            raise SystemExit(
                "NilVec is unavailable. Follow the source-build instructions in "
                "the README, or run with --backend exact."
            ) from error
        # Constructor verified against the linked upstream src/hnsw.rs.
        index = nilvec.PyHNSW(args.dimensions, 16, 200, 50, "euclidean", None)
        start = time.perf_counter()
        for vector in vectors:
            index.insert(vector)
        insertion_seconds = time.perf_counter() - start

    query_times = []
    recalls = []
    for query in queries:
        if index is None:
            start = time.perf_counter()
            exact_search(vectors, query, k)
            query_times.append(time.perf_counter() - start)
        else:
            # Ground truth is outside the timed approximate-search stage.
            truth = {i for _, i in exact_search(vectors, query, k)}
            start = time.perf_counter()
            results = index.search(query, k)
            query_times.append(time.perf_counter() - start)
            # NilVec returns f32-rounded vectors rather than IDs. Map each
            # returned vector to its closest original; exclude this work from
            # search timing. Duplicate results count only once in recall.
            found = {
                exact_search(vectors, vector, 1)[0][1]
                for _, vector in results
            }
            recalls.append(len(truth & found) / k)

    return {
        "backend": args.backend,
        "vectors": args.vectors,
        "dimensions": args.dimensions,
        "queries": args.queries,
        "k": k,
        "data_seed": args.seed,
        "insertion_seconds": insertion_seconds,
        "median_query_ms": statistics.median(query_times) * 1000,
        "mean_recall_at_k": statistics.mean(recalls) if recalls else None,
        "note": "Fresh synthetic-data measurement; not the historical 50x benchmark.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("exact", "nilvec"), default="exact")
    parser.add_argument("--vectors", type=positive_int, default=1000)
    parser.add_argument("--dimensions", type=positive_int, default=16)
    parser.add_argument("--queries", type=positive_int, default=10)
    parser.add_argument("--k", type=positive_int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    print(json.dumps(run(parser.parse_args()), indent=2))


if __name__ == "__main__":
    main()
