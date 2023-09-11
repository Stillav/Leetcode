class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for i in s:
            if i not in ss: 
                ss.add(i)
                print(ss)
            else: 
                ss.remove(i)
                print(ss)
        return len(s) - len(ss) + 1 if len(ss) != 0 else len(s) 