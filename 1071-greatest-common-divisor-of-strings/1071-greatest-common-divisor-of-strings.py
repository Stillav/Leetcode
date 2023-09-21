class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp = list()
        answer = ''
        if len(str2) < len(str1):
            str1, str2 = str2, str1 
            
        for s in str1:
            temp.append(s)
            
            if ''.join(temp)*(len(str1)//len(temp)) == str1 and ''.join(temp)*(len(str2)//len(temp)) == str2:
                answer = ''.join(temp)
            
        return answer