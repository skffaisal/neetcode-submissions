class Solution:
    def characterReplacement(self, n: str, k: int) -> int:
        # window_length - max Freq
        f={}
        l=0
        max_len=0
        for r in range(len(n)):
            f[n[r]]=f.get(n[r],0)+1
            
            while (r-l+1) - max(f.values())>k:
                f[n[l]]-=1
                l=l+1


            max_len=max(max_len,r-l+1)
        return max_len