class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(' ')
        i = -1
        while s_list[i] == '':
            i -=1
        return len(s_list[i])