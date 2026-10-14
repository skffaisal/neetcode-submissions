class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        min_len=float('inf')
        res_str=[-1,-1]
        
        count={}
        for i in range(len(t)):
            count[t[i]]=count.get(t[i],0)+1

        found=0
        required=len(count)
        l=0
        window={}
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            if s[r] in count and window[s[r]]==count[s[r]]:
                found+=1
            
            while found == required:

                if min_len > (r-l+1):
                    min_len = (r-l+1)
                    res_str = [l,r]
                
                if s[l] in count and window[s[l]]==count[s[l]]:
                    found-=1

                window[s[l]]-=1
                l=l+1

        l,r=res_str
        return s[l:r+1]

