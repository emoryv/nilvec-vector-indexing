# NilVec Vector Indexing — Case Study

**Research Project · Fall 2024**

I worked with a teammate and an industry mentor on a way to build vector-search indexes faster. My contribution was to the design of an optimistic concurrency approach. The optimization and measured improvement were shared project results.

## Reported project results

| Measure | Result |
| --- | --- |
| Dataset | 1,000,000 vectors |
| Earlier runtime | Approximately 400 seconds |
| Improved runtime | Approximately 8 seconds |
| Speedup | Approximately 50× |
| Runtime reduction | Approximately 98% |

The timings measure how long it took to build the index. The original hardware details, dataset, baseline code, and benchmark setup are not included, so the result has not been reproduced in this repository.

## Public source

[Upstream NilVec library](https://github.com/C0ll1nDr4k3/NilVec) · [Source fork](https://github.com/emoryv/NilVec) · [PyPI package](https://pypi.org/project/nilvec/)

- [Rust HNSW implementation](https://github.com/C0ll1nDr4k3/NilVec/blob/master/src/hnsw.rs)
- [Python bindings](https://github.com/C0ll1nDr4k3/NilVec/blob/master/src/lib.rs)
- [Benchmark script](https://github.com/C0ll1nDr4k3/NilVec/blob/master/main.py)

**About the code:** The linked library includes work by its original authors. My role was in the concurrency design; the source fork retains the original commit history. The current public code has not been verified as the version used for the timing comparison.

**Focus:** vector indexing, concurrency, systems performance

[Back to my profile](https://github.com/emoryv)
