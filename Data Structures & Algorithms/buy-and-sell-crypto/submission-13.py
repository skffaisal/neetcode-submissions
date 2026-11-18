class Solution:
    def maxProfit(self, n: List[int]) -> int:
        min_ele=n[0]
        max_profit=0

        for i in range(len(n)):
            min_ele=min(min_ele,n[i])

            max_profit=max(max_profit,n[i]-min_ele)
        return max_profit
            
