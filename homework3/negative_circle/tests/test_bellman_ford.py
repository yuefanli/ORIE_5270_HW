import unittest
from bellman_ford.bellman_ford import Bellman_Ford


class TestBellmanFord(unittest.TestCase):
    def test_no_c(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/negative_circle/tests'
        graph1 = Bellman_Ford(path + '/graph_no_c.txt')
        answer1 = None
        assert graph1.find_negative_circles() == answer1

    def test_pos_c(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/negative_circle/tests'
        graph2 = Bellman_Ford(path + '/graph_pos_c.txt')
        answer2 = None
        assert graph2.find_negative_circles() == answer2

    def test_neg_c(self):
        path = '/Users/liyuefan/Dropbox/ORIE_5270/ORIE_5270_HW/homework3/negative_circle/tests'
        graph3 = Bellman_Ford(path + '/graph_neg_c.txt')
        answer3 = [[6, 5, 7], [5, 7, 6], [7, 6, 5]]
        assert graph3.find_negative_circles() in answer3
