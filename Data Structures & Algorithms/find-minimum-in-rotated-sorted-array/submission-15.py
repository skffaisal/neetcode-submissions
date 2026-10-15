class Solution:
    def findMin(self, n: List[int]) -> int:
        
        l=0
        r=len(n)-1

        # ie the list is rotated 0 times, or rotated equal to the length of the list, so we got the original sorted array 
        if n[l]<n[r] : 
            return n[l]

        # if len(n)==1:
        #     return n[0]

        

        while l < r: # fails on l == r
            # when entered in the loop, that means the array has 2 sorted portions

            mid= (l+r)//2

            # ie the right portion of the list is not sorted, and n[mid] cannot be smallest because its clearly bigger then  right here
            if n[mid] > n[r]: 
                l=mid+1
            else: # here n[mid] is also a candidate for being the smallest
                r=mid

                


            

        return  n[r] # or n[l], becasue both are same 
