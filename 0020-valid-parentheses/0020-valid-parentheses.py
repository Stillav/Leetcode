class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for i, c in enumerate(s):
            if len(stack) == 0:
                stack.append(c)
                
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            
            elif c == ']' and stack[-1] == '[':
                stack.pop()
                
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            
            else:
                stack.append(c)
                
        return True if len(stack) == 0 else False