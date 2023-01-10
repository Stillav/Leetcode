class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = int(''.join(map(str, num))) + k 
        
        return (list(map(int, str(number))))