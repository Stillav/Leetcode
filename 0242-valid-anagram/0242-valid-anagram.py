class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {key: s.count(key) for key in s}
        t_dict = {key: t.count(key) for key in t}
        
        return s_dict.items() == t_dict.items()
        
        