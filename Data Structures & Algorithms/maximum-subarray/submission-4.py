class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        
        cum_sum=n[0]
        best=n[0]

        for i in range(1,len(n)):

            if n[i]>n[i]+cum_sum:
                cum_sum=n[i]
            else:
                cum_sum+=n[i]

            best=max(cum_sum,best)

        return best

            
