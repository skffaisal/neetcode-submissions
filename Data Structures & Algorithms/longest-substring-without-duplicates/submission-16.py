class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d={}

        l=0
        max_len=0
        for r in range(len(s)):

            if s[r] in d:
                l=max(l,d[s[r]]+1)
            
            d[s[r]]=r
            
            max_len=max(max_len, r-l+1)
        return max_len