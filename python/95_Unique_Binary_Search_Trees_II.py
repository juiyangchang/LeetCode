class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def node(val, left, right):
            new_node = TreeNode(val)
            new_node.left = left
            new_node.right = right
            return new_node
        
        def tree(left_lim, right_lim):
            tree_list = [node(val, left, right) for val in range(left_lim, right_lim+1)
                         for left in tree(left_lim, val-1) for right in tree(val+1, right_lim)] or [None]
            return tree_list
        
        if n:
            return tree(1, n)
        else:
            return []