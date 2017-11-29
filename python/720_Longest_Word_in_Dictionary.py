class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        seen = set([''])
        longest_word = ''
        
        for w in words:
            if w[:-1] in seen:
                seen.add(w)
                if len(w) > len(longest_word):
                    longest_word = w
                    
        return longest_word