# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        res = []
        queue = [(root, 0)]

        for node, depth in queue:
            if len(res) == depth:
                res.append(node.val)
            elif node.val > res[-1]:
                res[-1] = node.val

            if node.left:
                queue.append((node.left, depth+1))

            if node.right:
                queue.append((node.right, depth+1))

        return res
