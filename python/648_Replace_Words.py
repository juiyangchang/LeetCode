from collections import defaultdict

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        _trie = lambda: defaultdict(_trie)
        trie = _trie()
        
        for word in dict:
            cur = trie
            for char in word:
                cur = cur[char]
            cur['<END>'] = word
            
        def replace(word):
            cur = trie
            for char in word:
                cur = cur[char]
                if '<END>' in cur:
                    return cur['<END>']
            return word
        
        return ' '.join(map(replace, sentence.split()))