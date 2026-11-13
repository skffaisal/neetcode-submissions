class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0

        w={}

        max_len=0
        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1


            while (r-l+1)-max(w.values()) >k:
                w[s[l]]=w.get(s[l],0)-1
                l=l+1

            max_len=max(max_len,(r-l+1))
        return max_len
            