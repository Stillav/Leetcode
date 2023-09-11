class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        
        while ransomNote:
            if ransomNote[0] in magazine:
                magazine.remove(ransomNote.pop(0))
            else:
                return False
            
        return True 
        
        