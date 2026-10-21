"""Correctness checks for the exact reference and recall adapter."""

import argparse
import sys
import types
import unittest
from unittest.mock import patch

import demo


class SearchChecks(unittest.TestCase):
    def test_known_nearest_neighbors_and_ties(self):
        vectors = [[3.0, 4.0], [0.0, 0.0], [-3.0, -4.0]]
        self.assertEqual(demo.exact_search(vectors, [0.0, 0.0], 3),
                         [(0.0, 1), (5.0, 0), (5.0, 2)])

    def test_k_larger_than_dataset(self):
        self.assertEqual(demo.exact_search([[0.0]], [1.0], 5), [(1.0, 0)])

    def test_duplicate_approximate_results_do_not_inflate_recall(self):
        class FakeIndex:
            def __init__(self, *args):
                self.vectors = []

            def insert(self, vector):
                self.vectors.append(vector)

            def search(self, query, k):
                nearest = demo.exact_search(self.vectors, query, 1)[0]
                return [(nearest[0], self.vectors[nearest[1]])] * k

        args = argparse.Namespace(backend="nilvec", vectors=8, dimensions=2,
                                  queries=2, k=4, seed=42)
        with patch.dict(sys.modules, {"nilvec": types.SimpleNamespace(PyHNSW=FakeIndex)}):
            result = demo.run(args)
        self.assertEqual(result["mean_recall_at_k"], 0.25)


if __name__ == "__main__":
    unittest.main()
