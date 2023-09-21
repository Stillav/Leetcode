from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        return count1.keys() == count2.keys() and list(sorted(count1.values())) == list(sorted(count2.values()))