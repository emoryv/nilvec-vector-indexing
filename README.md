# NilVec — Vector Search Indexing Optimization

**Research Project · Fall 2024**

I co-designed an optimistic-concurrency approach for vector-search indexing in a **two-person team, with guidance from an industry mentor**. On a one-million-vector dataset, indexing runtime fell from approximately **400 seconds to 8 seconds**, an approximately **50× speedup**.

## Engineering problem

Vector-search systems need to build an index before they can efficiently retrieve nearby vectors. This project focused on reducing index-construction time through a different concurrency approach.

## My contribution

I co-designed the optimistic-concurrency approach with my teammate. The performance improvement was a shared project result; this write-up does not attribute the entire NilVec library to me.

## Reported result

| Measure | Result |
| --- | --- |
| Dataset size | 1,000,000 vectors |
| Earlier indexing runtime | Approximately 400 seconds |
| Improved indexing runtime | Approximately 8 seconds |
| Speedup | Approximately 50× (400 ÷ 8) |
| Timed-stage runtime reduction | Approximately 98% |

These figures describe the project's indexing measurement. They are not a claim of 50× faster search queries, a universal speedup across datasets, or an independently reproduced benchmark. Hardware, dataset distribution, and the benchmark harness are not included in this repository.

## Related project

[NilVec on PyPI](https://pypi.org/project/nilvec/)

[Source code fork](https://github.com/emoryv/NilVec) · [Original repository](https://github.com/C0ll1nDr4k3/NilVec)

## Repository scope

This repository documents my contribution to the indexing optimization. It is a portfolio case study rather than a copy of the original library, implementation, or benchmark dataset.

**Focus:** vector indexing, concurrency, systems performance, benchmarking

[Back to my profile](https://github.com/emoryv)
