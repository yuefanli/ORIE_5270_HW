import numpy as np
import heapq


class Dijkstra(object):
    def __init__(self, name_txt_file, source, destination):
        self.file = name_txt_file
        self.source = source
        self.destination = destination

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

    def find_shortest_path(self):
        """
        :return: S[self.destination] is a double type distance from source to destination
        """
        self.graph = self.read_txt_file()
        start_key = self.graph.keys()
        key = list(start_key)
        for k in start_key:
            v = self.graph[k]
            for dest, weight in v:
                if dest not in key:
                    key.append(dest)
                else:
                    pass
        d = {}
        for k in key:
            d[k] = np.inf
        d[self.source] = 0
        F = []
        heapq.heappush(F, (0, self.source))
        S = {}
        while len(F) > 0:
            f = heapq.heappop(F)
            S[f[1]] = f[0]
            # child: [(name_of_child_node, edge_between_node_to_child)]
            if f[1] in self.graph.keys():
                child = self.graph[f[1]]
            else:
                child = []
            curr_F = list(map(lambda x: x[1], F))
            curr_S = S.keys()
            # c stands for current child node, w stands for weight
            for c, w in child:
                if (c not in curr_F) and (c not in curr_S):

                    d[c] = d[f[1]] + w
                    heapq.heappush(F, (d[c], c))
                    curr_F = list(map(lambda x: x[1], F))
                else:
                    if d[f[1]] + w < d[c]:
                        d[c] = d[f[1]] + w
                        F = list(map(lambda x: (d[c], c) if x[1] == c else x, F))
                        heapq.heapify(F)
                    else:
                        pass
        if self.destination in S.keys():
            return S[self.destination]
        else:
            return np.inf
