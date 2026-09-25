class Solution:
    def maxSubArray(self, n: List[int]) -> int:

        cum_sum=n[0]
        max_sum=n[0]

        for i in range(1,len(n)):

            if n[i]>n[i]+cum_sum: # stop and start with the current elemt as cum_sum
                cum_sum=n[i]
            else:
                cum_sum+=n[i]

            if max_sum < cum_sum:
                max_sum=cum_sum
        return max_sum