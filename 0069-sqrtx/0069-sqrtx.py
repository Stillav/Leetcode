class Solution:
    def mySqrt(self, x: int) -> int:
        tail = x 
        start = 0 
        
        temp = (tail + start) >> 1
        
        while start <= tail:
            if temp * temp == x:
                return temp
            
            elif temp * temp < x:
                start = temp + 1
            
            elif temp * temp > x:
                tail = temp - 1 
            
            temp = (tail + start) >> 1
        
        return temp