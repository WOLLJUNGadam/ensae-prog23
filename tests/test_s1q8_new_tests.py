# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework


class Test_GraphCC(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.05.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4})})



class Test_Reachability(unittest.TestCase):
    def test_network1(self):
        g = graph_from_file("input/network.05.in")
        self.assertIn(g.get_path_with_power(2, 4, 7), [[2, 3, 4], [2, 3, 1, 4], [2,1,3,4], [2,1,4]])



class Test_MinimalPower(unittest.TestCase): 
    def test_network2(self):
        g = graph_from_file("input/network.05.in")
        self.assertEqual(g.min_power(2, 4)[1], 6)



if __name__ == '__main__':
    unittest.main()
