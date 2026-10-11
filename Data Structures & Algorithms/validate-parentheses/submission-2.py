class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'}

        stack = []
        

        for char in s:
            # 1. If opening bracket: push it
            if char not in pairs:
                stack.append(char)
            
            # 2. Otherwise: validate and pop
            elif stack and pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False 

        return not stack
