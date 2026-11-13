class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0

        w={}
        max_freq=0
        max_len=0
        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1
            max_freq= max(max_freq,w[s[r]])


            while (r-l+1)-max_freq >k:
                w[s[l]]=w.get(s[l],0)-1
                l=l+1

            max_len=max(max_len,(r-l+1))
        return max_len