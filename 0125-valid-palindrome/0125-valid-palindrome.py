class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphas = [spell.lower() for spell in s if spell.isalpha() or spell.isdigit()]
        
        result = True
        
        for i in range(len(alphas) //2):
            if alphas[i] != alphas[len(alphas) - i -1]:
                
                return False
        
        
        return result