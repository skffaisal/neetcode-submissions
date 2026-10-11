class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        
        cum_sum=n[0]
        best=n[0]

        for i in range(1,len(n)):

            cum_sum=max(cum_sum + n[i], n[i])

            best=max(cum_sum,best)

        return best

            
