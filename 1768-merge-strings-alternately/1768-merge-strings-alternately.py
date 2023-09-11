class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest
        
        answer = list()
        
        for w1, w2 in zip_longest(word1, word2):
            answer.append(w1 if w1 else '')
            answer.append(w2 if w2 else '')
            
        answer = ''.join(answer)
        
        return answer