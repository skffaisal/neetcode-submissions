class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        

        max_sum=n[0]
        cum_sum=n[0]
        for i in range(1,len(n)):
            if n[i]+cum_sum <n[i]:
                cum_sum=n[i]
            else:
                cum_sum+=n[i]
        
            max_sum=max(max_sum,cum_sum)
        return max_sum