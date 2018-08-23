class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, root):
        self.root = root

    def tree_print(self):
        """
        This function print out the binary tree
        :return: [[str, str], [str, str]]\
        matrix with all blanks and empty nodes filled in with '|'
        """
        thislevel = [self.root]
        whole_tree = []
        while thislevel:
            nextlevel = list()
            tmp_str = []
            if len(thislevel) != thislevel.count(None):
                for n in thislevel:
                    if n is not None:
                        tmp_str.append(str(n.value))
                        if n.left:
                            nextlevel.append(n.left)
                        else:
                            nextlevel.append(None)
                        if n.right:
                            nextlevel.append(n.right)
                        else:
                            nextlevel.append(None)
                    else:
                        tmp_str.append("h")
                        nextlevel.append(None)
                        nextlevel.append(None)
            else:
                break
            thislevel = nextlevel
            whole_tree.append(tmp_str)
        whole_tree_rev = whole_tree[::-1]
        tree_rev = []
        line_last = whole_tree_rev[0]
        N = len(line_last)
        for j in range(1, 2 * N - 1, 2):
            line_last.insert(j, "|")
        N = len(line_last)
        tree_rev.append(line_last)
        for i in range(1, len(whole_tree_rev)):
            cur_line = whole_tree_rev[i]
            tmp = ['|' for j in range(N)]
            left = []
            right = []
            tag = 0
            for j in range(len(line_last)):
                items = line_last[j]
                if items != "|" and tag % 2 == 0:
                    left.append(j)
                    tag += 1
                elif items != "|" and tag % 2 == 1:
                    right.append(j)
                    tag += 1
            idxs = map(lambda x, y: int(x + y) / 2, left, right)
            for idx in idxs:
                tmp[idx] = cur_line[idxs.index(idx)]
            tree_rev.append(tmp)
            line_last = tmp
        for i in range(len(tree_rev)):
            row = tree_rev[i]
            for j in range(len(row)):
                if row[j] == 'h':
                    row[j] = '|'
                else:
                    pass
        tree_rev = tree_rev[::-1]
        return tree_rev
