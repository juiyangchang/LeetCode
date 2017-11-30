class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """        
        def n_sum(num, start, end, N, target, sublist = []):
            if N == 2:
                i, j = start, end-1
                while i < j:
                    sub_sum = num[i] + num[j]
                    
                    if sub_sum == target:
                        res.append(sublist + [num[i], num[j]])
                        i += 1
                        j -= 1
                        
                        while num[i] == num[i-1] and i < end - 1:
                            i += 1
                        while num[j] == num[j+1] and j > start + 1:
                            j-= 1
                        
                    elif sub_sum < target:
                        i += 1
                    else:
                        j -= 1               
                
            else:
                for i in range(start, end):
                    if target < N*num[i] or target > N*num[end-1]:
                        break
                    if i > start and num[i] == num[i-1]:
                        continue
                    n_sum(num, i+1, end, N-1, target - num[i], sublist + [num[i]])
                    
        num = sorted(nums)
        res = []
        n_sum(num, 0, len(num), 4, target)
        return res