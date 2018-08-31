import unittest
import numpy as np
from mat_multi.pyspark_mat_mult import mat_multiplication

class TestMulti(unittest.TestCase):
    def test1(self):
        mat_mul = mat_multiplication()
        w, sc = mat_mul.mat_multi('./tests/mat_A_1.txt', './tests/vec_B_1.txt')
        w = w.collect()
        sc.stop()
        f = open('./tests/mat_A_1.txt')
        mat_A = f.readlines()
        f.close()
        mat_A = list(map(lambda x: eval('[' + x.replace('\n', '') + ']')[1:], mat_A))
        mat_A = np.matrix(mat_A)
        f = open('./tests/vec_B_1.txt')
        vec_B = f.readlines()
        f.close()
        vec_B = list(map(lambda x: eval('[' + x.replace('\n', '') + ']'), vec_B))
        vec_B = np.array(vec_B)
        answer = np.dot(mat_A, vec_B.T)
        answer = answer.tolist()
        w = [[w[i][1]] for i in range(len(w))]
        assert w == answer

    def test2(self):
        mat_mul = mat_multiplication()
        w, sc = mat_mul.mat_multi('./tests/mat_A_2.txt', './tests/vec_B_2.txt')
        w = w.collect()
        sc.stop()
        f = open('./tests/mat_A_2.txt')
        mat_A = f.readlines()
        f.close()
        mat_A = list(map(lambda x: eval('[' + x.replace('\n', '') + ']')[1:], mat_A))
        mat_A = np.matrix(mat_A)
        f = open('./tests/vec_B_2.txt')
        vec_B = f.readlines()
        f.close()
        vec_B = list(map(lambda x: eval('[' + x.replace('\n', '') + ']'), vec_B))
        vec_B = np.array(vec_B)
        answer = np.dot(mat_A, vec_B.T)
        answer = answer.tolist()
        w = [[w[i][1]] for i in range(len(w))]
        assert w == answer
