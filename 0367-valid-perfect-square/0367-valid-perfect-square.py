class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0 
        tail = num 
        
        temp = (start + tail) >> 1
        
        while start <= tail:
            
            if temp * temp == num:
                return True
            
            elif temp * temp > num:
                tail = temp - 1
                
            elif temp * temp < num:
                
                start = temp + 1 
                
            temp = (start + tail) >> 1
            
        return False