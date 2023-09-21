class Solution:
    def reverseVowels(self, s: str) -> str:
        mo_dict, ja_dict = dict(), dict()
        length = len(s)
        answer = list()
        
        for i, spell in enumerate(s):
            if spell.lower() in ['a', 'e', 'i', 'o', 'u']:
                mo_dict[i] = spell 
            else:
                ja_dict[i] = spell 
                
        mo_index = list(mo_dict.keys())
        
        for i in range(len(mo_index) // 2):
            mo_dict[mo_index[i]], mo_dict[mo_index[len(mo_index) - 1 - i]] = mo_dict[mo_index[len(mo_index) - 1 - i]], mo_dict[mo_index[i]]
            
        for i in range(length):
            if mo_dict.get(i):
                answer.append(mo_dict[i])
            else:
                answer.append(ja_dict[i])
                
        return ''.join(answer)