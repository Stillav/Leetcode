class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = list()
        
        for s in words:
            temp = str()
            for c in s:
                temp += mos[ord(c) - 97]
                
            result.append(temp)
            
        result = set(result)
        
        return len(result)