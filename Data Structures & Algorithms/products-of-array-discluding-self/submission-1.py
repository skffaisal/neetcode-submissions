class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        
        # calculating prefix mul

        res=[]

        prefix=[1]

        for i in range (len(n)):
            prefix.append(prefix[i]*n[i])

        suffix=[1]* (len(n)+1)

        for i in range (len(n)-1,-1,-1):
            suffix[i]=suffix[i+1]*n[i]
        
        for i in range (len(n)):
            res.append(prefix[i]*suffix[i+1])

        return res
