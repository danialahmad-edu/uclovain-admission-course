import unittest
from question1 import mat_to_list



class TestMatToList(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(mat_to_list([]), [])

    def test_single_node(self):
        self.assertEqual(mat_to_list([[0]]), [[]])

    def test_two_nodes_not_connected(self):
        self.assertEqual(mat_to_list([[0, 0], [0, 0]]), [[], []])

    def test_two_nodes_connected(self):
        self.assertEqual(mat_to_list([[0, 1], [0, 0]]), [[1], []])

    def test_multiple_nodes(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]
        self.assertEqual(mat_to_list(adj_mat), [[1, 3], [2], [0], [4], [3], []])


if __name__ == '__main__':
    unittest.main()