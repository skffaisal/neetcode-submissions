class Solution:
    def maxProfit(self, n: List[int]) -> int:
        
        min_ele=n[0]
        max_diff=0
        for i in range (1,len(n)):

            if min_ele > n[i]:
                min_ele= n[i]
            
            diff= n[i]- min_ele

            max_diff=max(max_diff,diff)
        return max_diff
