# NilVec Vector Indexing — Case Study

**Research Project · Fall 2024**

Co-designed an optimistic-concurrency approach to reduce vector-index construction time in a two-person team, with guidance from an industry mentor.

## My contribution

Worked with my teammate on the concurrency design. The optimization and its measured improvement were shared project outcomes.

## Reported indexing measurement

| Measure | Result |
| --- | --- |
| Dataset | 1,000,000 vectors |
| Earlier runtime | Approximately 400 seconds |
| Improved runtime | Approximately 8 seconds |
| Speedup | Approximately 50× |
| Runtime reduction | Approximately 98% |

These timings describe index construction, not search-query latency. The original hardware details, dataset specification, baseline implementation, and benchmark harness are not included here, so this repository does not independently reproduce the reported result.

## Public source

[Upstream NilVec library](https://github.com/C0ll1nDr4k3/NilVec) · [Source fork](https://github.com/emoryv/NilVec) · [PyPI package](https://pypi.org/project/nilvec/)

- [Rust HNSW implementation](https://github.com/C0ll1nDr4k3/NilVec/blob/master/src/hnsw.rs)
- [Python bindings](https://github.com/C0ll1nDr4k3/NilVec/blob/master/src/lib.rs)
- [Benchmark script](https://github.com/C0ll1nDr4k3/NilVec/blob/master/main.py)

**Source and attribution:** My contribution was collaborative algorithm design. The linked library preserves upstream authorship and commit history; its current implementation is not established here as the version behind the reported timing measurement.

## Supplemental example

[Vector-search example and setup](examples/README.md) provides an exact-search reference and an optional NilVec adapter. It was added with AI assistance during portfolio preparation in October 2026, separately from the original research. The default mode and three correctness checks passed; the optional NilVec backend remains untested in this environment.

**Focus:** vector indexing, concurrency, systems performance

[Back to my profile](https://github.com/emoryv)
