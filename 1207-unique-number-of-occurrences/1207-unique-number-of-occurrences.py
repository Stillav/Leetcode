from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        v_list = [v for v in Counter(arr).values()]
        
        return len(v_list) == len(set(v_list))