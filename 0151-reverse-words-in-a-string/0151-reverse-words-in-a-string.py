class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        answer = []
        while '  ' in s:
            s = s.replace('  ', ' ')
        
        word_list = s.split(' ')
        
        for i in range(len(word_list) - 1, -1, -1):
            answer.append(word_list[i])
            
        return ' '.join(answer)
        