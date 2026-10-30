class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l=0
        r=len(n)-1

        while l<r:
            
            curr_sum=n[r]+n[l]

            if curr_sum==target:
                return [l+1,r+1]

            elif l<r and curr_sum>target:
                r=r-1
            elif l<r and  curr_sum<target:
                l=l+1