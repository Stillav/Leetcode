class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(index, temp):
            
            if len(temp) == len(digits):
                result.append(temp)
                return
            
            for alpha in alphas[digits[index]]:
                dfs(index + 1, temp + alpha)
        
        alphas = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = list()
        temp = ''
        
        if not digits:
            return result 
        
        dfs(0, temp)
        
        return result
        
            
                
        