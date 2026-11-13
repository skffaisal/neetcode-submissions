class Solution:
    def search(self, n: List[int], target: int) -> int:
        l=0
        r=len(n)-1

        while l<=r:

            mid=(l+r)//2

            if target == n[mid]:
                return mid
            
            # n[l] n[mid] n[r]

            if n[mid] >= n[r]:
                if n[l]<=target<=n[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if n[mid]<=target<=n[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

