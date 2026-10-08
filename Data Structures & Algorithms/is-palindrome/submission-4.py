class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Constant space and linear time 

        left =0
        right =len(s)-1

        while left<right:
            # skip non alpha numeric numbers 

            while left <right and not s[left].isalnum():
                left=left+1
            
            while left<right and not s[right].isalnum():
                right=right-1

            if s[left].lower() != s[right].lower():
                return False

            left=left+1
            right=right-1
        
        return True