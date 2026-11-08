class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        
        prefix=[1]
        for i in range(len(n)):
            prefix.append(n[i]*prefix[i])


        suffix=1

        for i in range(len(n)-1,-1,-1):
            prefix[i]=prefix[i]*suffix
            suffix*=n[i]
        return (prefix[:-1])
        