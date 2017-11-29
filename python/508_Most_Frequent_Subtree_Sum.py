from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        count = defaultdict(int)
        def subtree_sum(node):
            if not node:
                return 0
            sub_sum = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            count[sub_sum] += 1
            return sub_sum
        
        subtree_sum(root)
        max_count = max(count.values())
        return [number for number in count if count[number] == max_count]