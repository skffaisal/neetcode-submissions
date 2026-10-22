class Solution:
    def search(self, n: List[int], target: int) -> int:
        l=0
        r=len(n)-1

        while l<=r:
            m=(l+r)//2

            if n[m]==target:
                return m

        # n[l]  n[m]  n[r]   
        
            if n[m]>=n[r]:
                if n[m]>=target>=n[l]:
                    r=m-1
                else:
                    l=m+1
            else:
                if n[m]<=target<=n[r]:
                    l=m+1
                else:
                    r=m-1

        return -1

