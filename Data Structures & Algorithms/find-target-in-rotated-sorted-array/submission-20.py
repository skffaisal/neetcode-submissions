class Solution:
    def search(self, n: List[int], target: int) -> int:
        l=0
        r=len(n)-1

        while l<=r:

            m=(l+r)//2

            if target==n[m]:
                print(n[m])
                return m
            
            if n[m]>=n[r]: # left side sorted
                if n[l]<=target<=n[m]:
                    r=m-1
                else:
                    l=m+1
            else: # right side sorted
                if n[m]<=target<=n[r]:
                    l=m+1
                else:
                    r=m-1
        return -1