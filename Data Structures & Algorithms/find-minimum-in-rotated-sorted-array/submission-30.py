class Solution:
    def findMin(self, n: List[int]) -> int:
        
        l=0
        r=len(n)-1

        while l<r:
            m=(l+r)//2

            if n[m]<n[r]:
                r=m
            elif n[m] > n[r]:
                l=m+1

        return n[l]