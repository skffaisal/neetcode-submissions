class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=0
        count={}

        max_len=0

        for r in range(len(s)):

            count[s[r]]=count.get(s[r],0)+1

            
            if r-l+1 - max(count.values()) >k:
                count[s[l]]-=1
                l=l+1

            max_len= max(max_len,r-l+1)
        
        return max_len

