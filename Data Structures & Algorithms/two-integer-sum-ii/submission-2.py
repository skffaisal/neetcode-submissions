class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        
        l=0
        r=len(n)-1
        
        while l<r:

            cur_sum=n[l]+n[r]

            if cur_sum==target:
                return [l+1,r+1]
            
            elif cur_sum>target:
                r=r-1
            elif cur_sum<target:
                l=l+1
         
            