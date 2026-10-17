class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str=''

        for i in range(len(s)):
            if s[i].isalnum():
                clean_str+=s[i].lower()

        return (clean_str)==(clean_str[::-1])

