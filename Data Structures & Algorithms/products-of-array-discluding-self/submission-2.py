class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        
        # calculating prefix mul

        res=[]

        prefix=[1]

        for i in range (len(n)):
            prefix.append(prefix[i]*n[i])

        suffix=1
        
        for i in range (len(n)-1,-1,-1):
            prefix[i]*=suffix
            suffix=suffix*n[i]
        prefix.pop()
        return prefix
