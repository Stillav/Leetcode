class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        else:
            x: str = str(x)
            for i, v in enumerate(str(x)):
                if v != x[len(x)-i-1]:
                    return False
                
            return True