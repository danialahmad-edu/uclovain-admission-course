import unittest
from question2 import reachable


class TestReachable(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(reachable([], 0), set())

    def test_single_node(self):
        self.assertEqual(reachable([[]], 0), {0})

    def test_two_nodes_not_connected(self):
        self.assertEqual(reachable([[], []], 0), {0})

    def test_two_nodes_connected(self):
        self.assertEqual(reachable([[1], []], 0), {0, 1})

    def test_multiple_nodes(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2, 3, 4})
        self.assertEqual(reachable(adj_list, 3), {3, 4})

if __name__ == '__main__':
    unittest.main()