class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def preorder(node):
            if not node:
                return ' *'
            else:
                return ' ' + str(node.val) + preorder(node.left) + preorder(node.right)
        
        return preorder(t) in preorder(s)