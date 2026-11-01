class Solution:
    def findMin(self, n: List[int]) -> int:
        
        l=0
        r=len(n)-1

        while l<r:
            mid=(l+r)//2

            if not n[mid]<=n[r]:
                l=l+1
            else:
                r=r-1
        return n[l]