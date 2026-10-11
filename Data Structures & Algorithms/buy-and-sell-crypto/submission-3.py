class Solution:
    def maxProfit(self, n: List[int]) -> int:
        
        max_diff=0
        min_ele=n[0]
        for i in range (len(n)):

            min_ele = min (min_ele,n[i])

            diff = n[i]-min_ele

            if max_diff < diff:
                max_diff = diff

        return max_diff



        