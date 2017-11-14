# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return

        queue = deque([node])
        copy_dict = {node: UndirectedGraphNode(node.label)}

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in copy_dict:
                    copy_dict[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)

                copy_dict[current].neighbors.append(copy_dict[neighbor])

        return copy_dict[node]
