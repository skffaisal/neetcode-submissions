class Solution:
    def isValid(self, s: str) -> bool:

        d={
            ')':'(',
            '}':'{',
            ']':'['
            }

        stack=[]
        for char in s:
            if char not in d:
                stack.append(char)
            elif stack and stack[-1] == d[char]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False


