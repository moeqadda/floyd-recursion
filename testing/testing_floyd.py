#!/usr/bin/env python3
import unittest
import sys
from recursive_floyd import shortest_path, floyd

# Test the function of recursion
class ShortPathTestCase(unittest.TestCase):
    """
    Test case for the 'shortest_path' function.
    """

    def test_shortest_path(self):
        """
        Test the 'shortest_path' function with a sample graph.
        """
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        result = shortest_path(0, 1, 3, graph)
        self.assertEqual(result, 7)


# Test the Floyd function
class FloydOutputTestCase(unittest.TestCase):
    """
    Test case for the 'floyd' function.
    """

    def test_floyd(self):
        """
        Test the 'floyd' function with a sample graph.
        """
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        MAX_LENGTH = len(graph[0])
        shortest_graph = [[0, 7, 12, 8],
                          [NO_PATH, 0, 5, 7],
                          [NO_PATH, NO_PATH, 0, 2],
                          [NO_PATH, NO_PATH, NO_PATH, 0]]
        result = floyd(graph)
        self.assertEqual(result, shortest_graph)

    def test_test_input_failure(self):
        """
        Test the 'shortest_path' function with incorrect input.
        If a string or a character is passed instead of an integer,
        the test should raise a TypeError.
        """
        NO_PATH = sys.maxsize
        graph = [[0, "x", NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        with self.assertRaises(TypeError):
            result = shortest_path(0, 1, 3, graph)

    def test_test_one_node(self):
        """
        Test the 'shortest_path' function with a single-node graph.
        The result should be 0 as there is only one node.
        """
        NO_PATH = sys.maxsize
        graph = [[0]]
        result = shortest_path(0, 0, 0, graph)
        self.assertEqual(result, 0)

    def test_node_path(self):
        """
        Test the 'shortest_path' function with a non-existent node.
        The test should raise an IndexError.
        """
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        with self.assertRaises(IndexError):
            result = shortest_path(0, 4, 0, graph)

    def test_non_intermediary_node(self):
        """
        Test the 'shortest_path' function with a non-existent intermediary node.
        The test should raise an IndexError.
        """
        NO_PATH = sys.maxsize
        graph
