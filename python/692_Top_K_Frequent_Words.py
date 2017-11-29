from collections import Counter, defaultdict
'''
https://discuss.leetcode.com/topic/106969/python-with-explanation
'''
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or k == 0:
            return []
        
        word_count = Counter(words)
        freq = defaultdict(list)
        
        for w, cnt in word_count.items():
            freq[cnt].append(w)
            
        res = []
        for i in range(len(words), 0, -1):
            if i in freq:
                res.extend([(w,i) for w in freq[i]])
            if len(res) >= k:
                break
                
        res.sort(key = lambda x: (-x[1], x[0]))
                
        return [el[0] for el in res[:k]]