# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework


class Test_MinimalPower(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file("input/network.00.in")
        a = g.kruskal()
        for node in g.nodes:
            # Network00 is already a tree
            self.assertEqual(set(a.graph[node]), set(g.graph[node]))

    def test_network01(self):
        g = graph_from_file("input/network.01.in")
        a = g.kruskal()
        for node in g.nodes:
            # Network01 is already composed by 2 trees
            self.assertEqual(set(a.graph[node]), set(g.graph[node]))

    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        a = g.kruskal()
        self.assertEqual(set(a.graph[1]), {(4, 4, 1)})
        self.assertEqual(set(a.graph[2]), {(3, 4, 1)})
        self.assertEqual(set(a.graph[3]), {(2, 4, 1), (4, 4, 1)})
        self.assertEqual(set(a.graph[4]), {(1, 4, 1), (3, 4, 1)})

    def test_network03(self):
        g = graph_from_file("input/network.03.in")
        a = g.kruskal()
        self.assertEqual(set(a.graph[1]), {(2, 10, 1)})
        self.assertEqual(set(a.graph[2]), {(3, 4, 1), (1, 10, 1)})
        self.assertEqual(set(a.graph[3]), {(2, 4, 1), (4, 4, 1)})
        self.assertEqual(set(a.graph[4]), {(3, 4, 1)})

    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        a = g.kruskal()
        self.assertEqual(set(a.graph[1]), {(2, 4, 89)})
        self.assertEqual(set(a.graph[2]), {(1, 4, 89), (3, 4, 3)})
        self.assertEqual(set(a.graph[3]), {(2, 4, 3), (4, 4, 2)})
        self.assertEqual(set(a.graph[4]), {(3, 4, 2)})

if __name__ == '__main__':
    unittest.main()
