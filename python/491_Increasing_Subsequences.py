class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        res = set()

        def dfs(idx, sub):
            if nums[idx] >= sub[-1]:
                res.add(tuple(sub + [nums[idx]]))
                if idx + 1 < len(nums):
                    dfs(idx + 1, sub + [nums[idx]])

            if idx + 1 < len(nums):
                dfs(idx + 1, sub)

        for i, n in enumerate(nums[:-1]):
            dfs(i+1, [n])

        return list(res)
