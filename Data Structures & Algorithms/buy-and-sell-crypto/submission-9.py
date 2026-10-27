class Solution:
    def maxProfit(self, n: List[int]) -> int:
        
        min_value=n[0]
        max_difference=0

        for i in range(len(n)):

            min_value=min(min_value,n[i])

            diff=n[i]-min_value

            max_difference=max(max_difference,diff)
        return max_difference