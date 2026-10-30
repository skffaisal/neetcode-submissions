class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        w=set()
        max_len=0
        for r in range(len(s)):
            while s[r] in w:
                w.discard(s[l])
                l=l+1 
                
            w.add(s[r])

            max_len=max(max_len,r-l+1)
        return max_len
            