class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_str=''
        min_len=float('inf')

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

                if min_len>(r-l+1):
                    min_len= (r-l+1)
                    res_str= s[l:r+1]

                
                if s[l] in count and window[s[l]]==count[s[l]]:
                    found-=1
                window[s[l]]=window.get(s[l],0)-1
                l=l+1

        return res_str


