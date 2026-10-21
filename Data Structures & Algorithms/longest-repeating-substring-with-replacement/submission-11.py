class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_len=0
        d={}
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1

            # if (r-l+1)-max(d.values()) <=k: valid 

            while (r-l+1)-max(d.values()) > k: # if not valid, make it valid
                d[s[l]]=d.get(s[l],0)-1
                l=l+1
            max_len=max(max_len,r-l+1)
        return max_len




                