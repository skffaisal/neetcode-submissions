class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for words in strs:
            res+=str(len(words))+'|'+words
        return res

    def decode(self, s: str) -> List[str]:


        l=0

        r=0
        res=[]
        while r<len(s): 
            if s[r]=='|':
                leng=int(s[l:r])
                r=r+1
                res.append(s[r:r+leng])
                r=r+leng
                l=r
            else:
                r=r+1
        return (res)