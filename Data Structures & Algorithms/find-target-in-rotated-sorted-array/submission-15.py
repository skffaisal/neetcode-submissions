class Solution:
    def search(self, n: list[int], target: int) -> int:
        l=0
        r=len(n)-1

        while l<=r:

            m=(l+r)//2

            if target==n[m]:
                return m

            # Identify the sorted half 
            if n[l] <= n[m]: # left half is sorted 
                if n[l]<=target<=n[m]: # check whether the target belongs to that half
                    r=m-1 # already checked index m, and it was not the target 
                else:
                    l=m+1
            else:# right half is sorted ie n[m] <= n[r]
                if n[m]<=target<=n[r]:
                    l=m+1
                else:
                    r=m-1
                


        return -1





