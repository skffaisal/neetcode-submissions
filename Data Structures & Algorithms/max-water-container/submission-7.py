class Solution:
    def maxArea(self, n: List[int]) -> int:
        l=0
        r=len(n)-1
        max_area=0
        while l<r:
            length=min(n[l],n[r])
            width=r-l
            area=length * width
            max_area=max(max_area,area)
            if n[l]<n[r]:
                l=l+1
            else:
                r=r-1
        return max_area


