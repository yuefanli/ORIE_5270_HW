import copy
import numpy as np


class Bellman_Ford(object):
    def __init__(self, name_txt_file):
        """
        :param name_txt_file: str of input txt file name
        """
        self.file = name_txt_file

    def read_txt_file(self):
        graph = {}
        with open(self.file) as f:
            tag = 0
            for l in f:
                if tag % 2 == 0:
                    tmp_key = int(l.replace('\n', ''))
                    tag += 1
                elif tag % 2 == 1:
                    if l[0] == '(':
                        tmp_value = eval('[' + l.replace('\n', '') + ']')
                        graph[tmp_key] = tmp_value
                        tag += 1
                    else:
                        graph[tmp_key] = []
                        tmp_key = int(l.replace('\n', ''))

                else:
                    pass
        return graph

    def find_negative_circles(self):
        """
        :return: negative_c: [int, int] list of nodes included in negative circle
                 empty list if no negative circle
        """
        self.graph = self.read_txt_file()
        start_key = self.graph.keys()

        edges = []
        key = list(start_key)
        for k in start_key:
            v = self.graph[k]
            for dest, weight in v:
                edges.append((k, dest, weight))
                if dest not in key:
                    key.append(dest)
                else:
                    pass
        # pi records the parent node
        pi = {}
        V = len(key)
        d = {}
        for k in key:
            d[k] = np.inf
            pi[k] = k

        negative_c = []
        # then randomly choose starting point to go through Bellman-Ford
        for k in key:
            d[k] = 0

            for _ in range(V - 1):
                # s for starting vertix, e for ending, w for weight
                for s, e, w in edges:
                    # the distance from certain parent node smaller than original minimum
                    if d[s] + w < d[e]:
                        d[e] = d[s] + w
                        pi[e] = s
                    else:
                        continue

            d_v_1 = copy.deepcopy(d)
            # the extra round for detecting negative circle
            for s, e, w in edges:
                # the distance from certain parent node smaller than original minimum
                if d[s] + w < d[e]:
                    d[e] = d[s] + w
                    pi[e] = s
                else:
                    continue
            for node in d.keys():
                if d_v_1[node] > d[node]:
                    path = [node]
                    cur_node = node
                    last_node = pi[cur_node]
                    for _ in range(V):
                        path.append(last_node)
                        cur_node = last_node
                        last_node = pi[cur_node]
                    if len(set(path)) < len(path):
                        cnt = {}
                        for n in set(path):
                            cnt[n] = 0

                        for i in range(len(path)):
                            cnt[path[i]] += 1
                            if cnt[path[i]] == 2:
                                negative_c = path[path.index(path[i])+1:(i + 1)]
                                negative_c = negative_c[::-1]
                                return negative_c
                            else:
                                continue
                    else:
                        print('wrong! negative circle detected but not found!')
                else:
                    print('path: ', (k, node), ' is OK!')
        return negative_c
