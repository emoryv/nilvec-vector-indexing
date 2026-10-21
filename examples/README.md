# Vector-search demo

A small runnable companion to the [NilVec project case study](../README.md).
The default mode uses only Python's standard library: it creates seeded synthetic
vectors and runs an exact Euclidean nearest-neighbor search. An optional adapter
compares NilVec search results with that exact reference using recall@k.

This example was added with AI assistance during portfolio preparation in October
2026. It is separate from the original research implementation and does not
reproduce or substantiate the historical 400-to-8-second result. The original
library and its authorship remain in the [upstream repository](https://github.com/C0ll1nDr4k3/NilVec).

## Run immediately

Requires Python 3.10 or later. From this repository's root:

```sh
python examples/demo.py
python examples/demo.py --vectors 2000 --dimensions 32 --queries 20 --k 10
python -m unittest discover -s examples -v
```

On systems that use `python3`, substitute it for `python`.
Output is JSON containing the dataset settings and median query time in milliseconds.
In exact mode, insertion time and recall are `null`: the reference scans the
vectors directly and no approximate-search comparison is performed.

## Optional: run against NilVec

Requires a Rust toolchain and an isolated Python environment. Build the linked
upstream snapshot, then return to this repository:

```sh
python -m venv .venv
# Activate: source .venv/bin/activate (macOS/Linux)
# Activate: .venv\Scripts\Activate.ps1 (Windows PowerShell)
python -m pip install maturin==1.8.2
git clone https://github.com/C0ll1nDr4k3/NilVec.git ../nilvec-upstream
git -C ../nilvec-upstream checkout 45a7464265
python -m maturin develop --release --manifest-path ../nilvec-upstream/Cargo.toml
python examples/demo.py --backend nilvec
```

The adapter follows `PyHNSW(dim, m, ef_construction, ef_search, metric, schema)`
in that snapshot's `src/hnsw.rs`, using the Euclidean metric and no metadata.
The constructor's signature differs from some upstream README examples.

## Measurements and limits

- Data generation and exact ground-truth calculation are outside NilVec timings.
- Insertion time covers the insertion loop; query time covers each search call.
- Recall@k measures overlap with exact nearest-neighbor IDs. Repeated approximate
  results count once. The library returns rounded vectors rather than IDs, so
  this demo maps each result to its nearest original vector outside search timing.
  Use these small synthetic datasets; ID recovery is intentionally simple and
  is unsuitable for duplicate vectors or large production benchmarks.
- The seed fixes input vectors and queries. NilVec's internal randomness and
  machine load can still affect results. Timings are observations, not assertions.
- This is a search example, not a comparison of old and new concurrency algorithms.

## Verification

The standard-library mode and correctness checks were run locally on Python 3.12.
All three checks passed; a run with 1,000 vectors, 16 dimensions, and 10 queries
completed successfully. The tests cover known neighbors, ties, oversized k, and
duplicate-result handling in the optional adapter using a test double.

The real NilVec build and optional backend have not been executed in this environment;
no compatible 0.1.8 binary was available for the Windows runtime. The source-build
path above is provided for that optional integration and may require
platform-specific build fixes.
