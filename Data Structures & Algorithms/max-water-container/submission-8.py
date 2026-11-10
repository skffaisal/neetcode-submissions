class Solution:
    def maxArea(self, n: List[int]) -> int:
        
        l=0
        r=len(n)-1
        res=0

        while l<r:

            res= max(res,min(n[l],n[r]) * (r-l))

            if n[l]<n[r]:
                l=l+1
            else:
                r=r-1
        return res
