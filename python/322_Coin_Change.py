from collections import defaultdict
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        
        edges = coins[::-1]
        
        queue = [amount]
        visited = defaultdict(int)        
        visited[amount] = 0
        
        for v in queue:
            for e in edges:
                new_val = v - e
                if new_val == 0:
                    return visited[v] + 1
                elif new_val > 0 and new_val not in visited:
                    visited[new_val] = visited[v] + 1
                    queue.append(new_val)
        return -1