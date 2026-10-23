class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for char in strs:
            res+=str(len(char))+'|'+char
            
        return res

    def decode(self, s: str) -> List[str]:

        b=0
        res=[]
        i=0
        while i<len(s):
            if s[i]=="|":
                lent=int(s[b:i])
              
                i=i+1
                res.append(s[i:i+lent])
        
                i=i+lent
                b=i
            i=i+1
        return res


