class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ind=(-1,-1)

        freq={}
        for ele in t:
            freq[ele]=freq.get(ele,0)+1

        need=len(freq)
        have=0

        l=0
        w={}

        min_len=float('inf')

        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1

            if s[r] in freq and w[s[r]]==freq[s[r]]:
                have+=1
            
            while have == need:
                if r-l+1 < min_len:
                    min_len=r-l+1
                    ind=(l,r+1)

                if s[l] in freq and w[s[l]]==freq[s[l]]:
                    have-=1                

                w[s[l]]=w.get(s[l],0)-1
                l=l+1
        l,r=ind
        return (s[l:r])
            

