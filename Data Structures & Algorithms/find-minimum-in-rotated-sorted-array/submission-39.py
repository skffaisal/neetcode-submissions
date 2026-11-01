class Solution:
    def findMin(self, n: List[int]) -> int:
        
        l=0
        r=len(n)-1
        min_value=float('inf')
        while l<=r:
            mid=(l+r)//2
            min_value=min(min_value,n[mid])
            if not n[mid]<=n[r]:
                l=mid+1
            else:
                r=mid-1
        return min_value
        # return n[l]