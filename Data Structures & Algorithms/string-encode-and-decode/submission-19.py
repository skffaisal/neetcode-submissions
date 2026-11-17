class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for words in strs:
            res+=str(len(words))+'|'+words
        return res

    def decode(self, s: str) -> List[str]:
        print(s)

        l=0

        r=0
        res=[]
        while r<len(s):
            while s[r]!="|":
                r=r+1
                continue
            length = int (s[l:r])

            r=r+1
            res.append(s[r:r+length])
            r=r+length
            l=r

        return (res)


