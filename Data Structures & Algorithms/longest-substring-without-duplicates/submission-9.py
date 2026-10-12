class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # Instead of removing characters one by one when we see a repeat, we can jump the left pointer directly to the correct position.
        l=0
        mp={}
        max_len=0

        for r in range(len(s)):

            
           
           
            if s[r] in mp:
                l= max(mp[s[r]]+1,l)
            
            mp[s[r]]=r

            max_len=max(max_len,r-l+1)
        
        return max_len