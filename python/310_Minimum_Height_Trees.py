from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        if n == 2:
            return [0, 1]

        num_nodes = n

        adj = defaultdict(list)

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        leaves = [i for i in adj if len(adj[i]) == 1]

        while num_nodes > 2:
            num_nodes -= len(leaves)
            new_leaves = []

            for l in leaves:
                for n in adj[l]:
                    adj[n].remove(l)

                    if len(adj[n]) == 1:
                        new_leaves.append(n)

            leaves = new_leaves

        return leaves
