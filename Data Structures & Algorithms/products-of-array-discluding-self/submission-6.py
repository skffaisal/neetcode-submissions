class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        
        prefix=[1]
        for i in range (0,len(n)):
            prefix.append(prefix[i]*n[i])

        # print(prefix)

        suffix=[1]* (len(n)+1)

        for i in range(len(n)-1,-1,-1):
            suffix[i]=suffix[i+1]*n[i]

        # print(suffix)

        res=[]
        for i in range (len(n)):
            res.append(prefix[i]*suffix[i+1])

        # print(res)

        return res