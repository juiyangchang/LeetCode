class Solution:
    def canIWin(self, max_choosable, desired):
        """
        :type max_choosable: int
        :type desired: int
        :rtype: bool
        """
        
        def helper(nums, desired, current, cache):
            hashing = hash(tuple(nums))
            
            if hashing in cache:
                return cache[hashing]
            
            if nums[-1] + current >= desired:
                cache[hashing] = True
                return True
            elif any(not helper(nums[:i] + nums[i+1:], desired, current+nums[i], cache) 
                     for i in range(len(nums))):
                cache[hashing] = True
                return True
            
            cache[hashing] = False
            return False
        
        if (1 + max_choosable) * max_choosable < desired * 2:
            return False
        return helper(list(range(1, max_choosable+1)), desired, 0, {})      