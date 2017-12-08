class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        inc = None
        ans = 1
        tail = nums[0]
        
        for n in nums[1:]:
            if n != tail:
                if inc != (n > tail):
                    inc = n > tail
                    ans += 1
                # n is either representing new wiggling direction or a better last
                # number for the previous wiggling direction
                tail = n
        return ans