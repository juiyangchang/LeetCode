# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left, right):
            if bool(left) != bool(right):
                return False
            elif left is None:
                return True
            else:
                if left.val != right.val:
                    return False
                else:
                    return helper(left.left, right.right) and helper(left.right, right.left)

        if root:
            return helper(root.left, root.right)
        else:
            return True
