class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAAlnum(char):
            if (ord('A')<=ord(char)<=ord('Z')) or (ord('a')<=ord(char)<=ord('z')) or (ord('0')<=ord(char)<=ord('9')):
                return True
            else:
                return False
        l=0
        r=len(s)-1

        while l<r:
            while l<r and not isAAlnum(s[l]):
                l=l+1
            while l<r and not isAAlnum(s[r]):
                r=r-1

            if s[l].lower()!=s[r].lower():
                return False

            l=l+1
            r=r-1

        return True

