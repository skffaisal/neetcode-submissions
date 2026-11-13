class Solution:
    def findMin(self, n: List[int]) -> int:
        l=0
        r=len(n)-1

        while l<r:

            mid=(l+r)//2

            # n[l] n[mid] n[r]

            if n[mid] > n[r]:
                l=mid+1
            else:
                r=mid
        return n[l]