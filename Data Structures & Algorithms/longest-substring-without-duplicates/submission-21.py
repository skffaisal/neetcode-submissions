class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        l=0

        win={}

        for r in range(len(s)):
            

            if s[r] in win:
                l=max(l,win[s[r]]+1)

            win[s[r]]=r

            max_count=max(max_count,r-l+1)
        return max_count