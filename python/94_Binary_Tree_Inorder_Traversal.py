# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        ret = []        
        stack = []  
        node = root
        
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ret.append(node.val)
                node = node.right
        return ret