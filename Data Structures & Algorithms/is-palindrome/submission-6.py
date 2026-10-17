class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str=''

        for i in range(len(s)):
            if s[i].isalnum():
                clean_str+=s[i].lower()

        print(clean_str)

        l=0
        r=len(clean_str)-1

        while l<r:

            if clean_str[l]!=clean_str[r]:
                return False

            l=l+1
            r=r-1

        return True
