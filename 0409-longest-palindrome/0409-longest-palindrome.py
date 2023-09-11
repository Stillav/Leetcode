class Solution:
    def longestPalindrome(self, s: str) -> int:
        spell_list = list(s)
        spell_dict = {spell: spell_list.count(spell) for spell in spell_list}
        answer = 0
        one_odd = False 
        for key in spell_dict:
            if spell_dict[key] % 2 != 0 and not one_odd:
                one_odd = True
                answer += 1
                
            answer += spell_dict[key] if spell_dict[key] % 2 == 0 else spell_dict[key] - 1
        
        return answer 