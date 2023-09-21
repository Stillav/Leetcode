class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        answer = []
        while '  ' in s:
            s = s.replace('  ', ' ')
        
        word_list = s.split(' ')
            
        return ' '.join(word_list[::-1])
        