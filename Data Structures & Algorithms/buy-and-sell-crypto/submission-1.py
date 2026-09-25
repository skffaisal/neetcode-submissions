class Solution:
    def maxProfit(self, n: List[int]) -> int:

        min_val=n[0] # coz of negative inputs
        best_diff= 0 # becasue we want profit 

        for i in range(len(n)):

            if min_val >n[i]:
                min_val=n[i]
        
            diff = n[i]-min_val

            if best_diff< diff:
                best_diff =diff

        return best_diff
        