import unittest
import numpy as np
from dijkstra.dijkstra import Dijkstra


class TestBellmanFord(unittest.TestCase):
    def test_1(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/dijkstra/tests'
        graph1 = Dijkstra(path + '/graph_no_c.txt', 1, 5)
        answer1 = 1
        assert graph1.find_shortest_path() == answer1

    def test_2(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/dijkstra/tests'
        graph2 = Dijkstra(path + '/graph_pos_c.txt', 1, 8)
        answer2 = 10
        assert graph2.find_shortest_path() == answer2

    def test_3(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/dijkstra/tests'
        graph3 = Dijkstra(path + '/graph_pos_c.txt', 2, 1)
        answer3 = np.inf
        assert graph3.find_shortest_path() == answer3

    def test_4(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/dijkstra/tests'
        graph4 = Dijkstra(path + '/graph_pos_c.txt', 4, 5)
        answer4 = 5
        assert graph4.find_shortest_path() == answer4
