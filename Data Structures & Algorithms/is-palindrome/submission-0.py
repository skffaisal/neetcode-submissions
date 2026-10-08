class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str=""

        for char in s:
            if ('A'<=char<='Z') or ('a'<=char<='z') or ('0'<=char<='9'):
                cleaned_str=cleaned_str+char.lower()

        print(cleaned_str)
        if cleaned_str == cleaned_str[::-1]:
            return True
    
        return False