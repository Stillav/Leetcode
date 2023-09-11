class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter 
        
        magazine_dict = dict(Counter(magazine))
        
        for key in ransomNote:
            
            if magazine_dict.get(key):
                magazine_dict[key] -= 1
                if magazine_dict[key] == 0:
                    del magazine_dict[key]
            else:
                return False
            
        return True 
        
        