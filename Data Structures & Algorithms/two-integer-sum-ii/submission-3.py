class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l=0
        r=len(n)-1

        while l<r:
            cum_sum=n[l]+n[r]

            if target==cum_sum:
                return [l+1,r+1]
            elif target<cum_sum:
                r=r-1
            else:
                l=l+1
        return 