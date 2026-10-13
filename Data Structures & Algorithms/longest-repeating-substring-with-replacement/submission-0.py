class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=0

        freq={}

        max_length=0

        for r in range(len(s)):

            freq[s[r]]=freq.get(s[r],0)+1
            
            window_length = r-l+1
            max_freq= max(freq.values())

            while window_length - max_freq > k:
                freq[s[l]]=freq.get(s[l],0)-1
                l=l+1
                window_length = r-l+1

            max_length= max(max_length,window_length)
        
        return max_length










