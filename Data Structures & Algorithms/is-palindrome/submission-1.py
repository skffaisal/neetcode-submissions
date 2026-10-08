class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str=""

        for char in s:
            if char.isalnum():
                cleaned_str=cleaned_str+char.lower()
        print(cleaned_str)

        left =0
        right =len(cleaned_str)-1
        
        while left < right:
            if cleaned_str[left] != cleaned_str[right]:
                return False

            left=left+1
            right=right-1
        
        return True