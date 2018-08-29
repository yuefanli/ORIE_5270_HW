from pyspark import SparkContext
import numpy as np


def find_dis_c(centroids):
    def find_dists(point):
        c_tag = -1
        for cent in centroids:
            dis = 0
            c_tag += 1
            for p, c in zip(point, cent):
                dis += (p - c) ** 2
            yield (c_tag, np.sqrt(dis))

    return find_dists


def point_cent_pair_pass_func(find_dists):
    def point_cent_pair(point):
        p_c_pair = find_dists(point)
        d_all = []
        for c, d in p_c_pair:
            d_all.append(d)
        return (np.argmin(d_all), point)

    return point_cent_pair


def pyspark_kmeans(data_file, centroids_file, MAX_ITER=100):
    sc = SparkContext('local[4]', 'pyspark tutorial')
    # Load the data
    data = sc.textFile(data_file).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).cache()

    # Load the initial centroids
    centroids1 = sc.textFile(centroids_file).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).collect()
    for _ in range(MAX_ITER):
        find_dists = find_dis_c(centroids1)
        point_cent_pair = point_cent_pair_pass_func(find_dists)

        p_c = data.map(point_cent_pair)

        p_c_cnt = p_c.map(lambda x: (x[0], (1, x[1]))).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

        p_c_cnt = p_c_cnt.mapValues(lambda x: x[1] / x[0]).collect()

        centroids1 = list(map(lambda x: x[1], p_c_cnt))
    out_put = 'centroids_final.txt'
    f = open(out_put, 'w')
    for items in centroids1:
        items = str(list(items)).replace(',', ' ').replace('[', '').replace(']', '') + '\n'
        f.write(items)
    f.close()

    # return centroids1


if __name__ == "__main__":
    pyspark_kmeans('data.txt', 'c1.txt')
