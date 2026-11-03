class Solution:

    def encode(self, strs: List[str]) -> str:

        res=""
        for ele in strs:
            res+=str(len(ele))+'|'+ele
        return res

    def decode(self, s: str) -> List[str]:

        # print(s)
        res=[]
        l=0
        r=0
        while r <len(s):

            while s[r]!= '|':
                r+=1
            length= int(s[l:r])

            r=r+1
            res.append(s[r:r+(length)])

            r=r+length
            l=r
     


        return res


            