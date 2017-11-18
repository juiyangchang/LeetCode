class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        ref: https://discuss.leetcode.com/topic/72569/java-dfs-solution-with-various-optimizations-sorting-sequential-partition-dp/2
        """
        def backtracking(i, tot):
            if tot == 0:
                return True
            if i == len(num):
                return False

            if mask[i] and num[i] <= tot:
                mask[i] = False
                if backtracking(i + 1, tot - num[i]):
                    return True
                mask[i] = True

            return backtracking(i + 1, tot)


        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False

        num = sorted(nums, reverse=True)
        mask = [True]*len(nums)
        target = sum(nums) / 4

        for _ in range(4):
            if not backtracking(0, target):
                return False

        return True
