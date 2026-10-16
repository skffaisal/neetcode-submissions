class Solution:
    def search(self, n: list[int], target: int) -> int:
        
        l=0
        r=len(n)-1

        # first find the smallest element 
        while l < r: 

            m=(l+r)//2
            
            if n[m]>n[r]:
                l=m+1
            else:
                r=m

        min_index = l

        if min_index == 0: # ie min is at the 0th index, means the complete array is already sorted
            l = 0
            r = len(n) - 1
        elif n[0] <= target <= n[min_index-1]: # because n[min_index] is the first element of the right sorted portion
            l=0
            r=min_index-1            
        else:
            l=min_index
            r=len(n)-1 # important to assign again , becase after first while loop, ris equal to l here

        # considering only the sorted half which contains the target,and applying binary search
        while l <=r: # the target might be at the very last remaining index ie l==r
            
            m=(l+r)//2
            if target == n[m]:
                return m
            elif target > n[m]:
                l=m+1
            else:
                r=m-1
        return -1