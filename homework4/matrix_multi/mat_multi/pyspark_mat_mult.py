from pyspark import SparkContext

class mat_multiplication(object):
    def index_col(self,x):
        for n in range(len(x)): yield (n, x[n])

    def mat_multi(self, mat_A, mat_B):
        """
        :param mat_A: str file name of matrix A
        :param mat_B: str file name of vector B
        :return: W is RDD object, sc is sparkcontext object
        """
        sc = SparkContext('local[2]', 'pyspark matrix mult')
        A = sc.textFile(mat_A).map(eval).map(lambda x: (x[0], x[1:]))
        B = sc.textFile(mat_B).map(eval)
        B = B.flatMap(self.index_col)
        A = A.flatMapValues(self.index_col).map(lambda x: (x[1][0], (x[0], x[1][1])))
        W = A.join(B)
        W = W.map(lambda x: (x[1][0][0], x[1][0][1] * x[1][1]))
        W = W.reduceByKey(lambda x, y: x + y)
        return W, sc