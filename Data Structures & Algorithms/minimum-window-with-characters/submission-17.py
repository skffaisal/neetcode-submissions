class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l=0
        r=len(s)-1
        min_len=float('inf')
        res=""

        freq_t={}
        for char in t:
            freq_t[char]=freq_t.get(char,0)+1

        required=len(freq_t)
        have=0

        window={}

        for r in range(len(s)):

            window[s[r]]=window.get(s[r],0)+1

            if s[r]  in freq_t and window[s[r]]==freq_t[s[r]]:
                have+=1



            while have == required: # want to make this false
                if min_len > r-l+1:
                    min_len=r-l+1
                    res=s[l:r+1]    

                window[s[l]]=window.get(s[l],0)-1

                if s[l]  in freq_t and window[s[l]]<freq_t[s[l]]:
                    have-=1
                
                l=l+1

        return res
                

            