class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        res=""

        min_len=float('inf')

        l=0

        d={}
        for i in range(len(t)):
            d[t[i]]=d.get(t[i],0)+1


        
        w={}

        found=0
        have=len(d)

        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0)+1

            if s[r] in d and w[s[r]]==d[s[r]]:
                found+=1
            
            while found == have:

                if min_len > r-l+1:
                    min_len=r-l+1
                    res=s[l:r+1]

                
                if s[l] in d and w[s[l]]==d[s[l]]:
                    found-=1
                
                w[s[l]]=w.get(s[l],0)-1
                l=l+1
        return res




