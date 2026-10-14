class Solution:
    def maxProfit(self, n: list[int]) -> int:
        
        l=0
        profit=0
        for r in range(len(n)):

            if n[r]>n[l]:
                profit=max(profit,n[r]-n[l])
            else:
                l=r
        return profit
        