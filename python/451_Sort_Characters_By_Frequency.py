from collections import Counter
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([char*count for char, count in sorted(Counter(s).items(), key=lambda x:x[1], reverse=True)])