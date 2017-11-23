class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if not nums1 and not nums2:
            return 0.0
        
        tot = len(nums1) + len(nums2)
        
        if tot % 2 == 1:
            return self.findKth(nums1, nums2, tot // 2)
        else:
            return (self.findKth(nums1, nums2, (tot - 1) // 2) + self.findKth(nums1, nums2, tot // 2)) / 2.
                    
        
    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        mid1, mid2 = len(nums1) // 2, len(nums2) // 2
        m1, m2 = nums1[mid1], nums2[mid2]
        
        if k > mid1 + mid2:
            if m1 > m2:
                return self.findKth(nums1, nums2[mid2+1:], k - mid2 - 1)
            else:
                return self.findKth(nums1[mid1+1:], nums2, k - mid1 - 1)            
        else:
            if m1 > m2:
                return self.findKth(nums1[:mid1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:mid2], k)  