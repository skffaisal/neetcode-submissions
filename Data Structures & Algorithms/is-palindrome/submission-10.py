class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cs=""

        # for i in range(len(s)):
        #     if s[i]

        l=0
        r=len(s)-1

        while l<r:
            while l<r and not s[l].isalnum():
                l=l+1
            while l<r and not s[r].isalnum():
                r=r-1
            
            if s[l].lower()!=s[r].lower():
                return False
            l=l+1
            r=r-1
        return True