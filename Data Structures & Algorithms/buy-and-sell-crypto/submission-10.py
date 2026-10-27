class Solution:
    def maxProfit(self, n: List[int]) -> int:
        l=0
        max_profit=0
        for r in range(0,len(n)):

            if n[l]>n[r]:
                l=r
            

            diff = n[r]-n[l]
            max_profit= max(max_profit,diff)
        return max_profit