class Solution:
    def findMin(self, n: list[int]) -> int:
        
        l=0
        r=len(n)-1

        res= float('inf')

        while l<=r:
            m=(l+r)//2

            res=min(res,n[m])

            if n[m]>n[r]:
                l=m+1
            else: # ie  n[m] < n[r] , so m is also a candidate
                r=m-1

        return res