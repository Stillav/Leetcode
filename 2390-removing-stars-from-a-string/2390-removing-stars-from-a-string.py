class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for spell in s:
            if spell == '*':
                answer.pop(-1)
            else:
                answer.append(spell)
                
        return ''.join(answer)