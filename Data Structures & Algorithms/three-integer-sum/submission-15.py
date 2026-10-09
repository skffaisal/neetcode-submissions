class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        # keep one fixed, find the other 2 using two sum technique
        # pointer approach
        
        n.sort() # helps avoid duplicates

        res=[]

        for i in range(len(n)):

            if i > 0 and n[i] == n[i - 1]:  # Skip duplicates for the first element (outer loop)
                continue

            target= -(n[i])

            left=i+1
            right=len(n)-1



            while left < right:

                cur_sum= n[left]+n[right]

                if cur_sum == target:
                    
                    res.append([n[i],n[left],n[right]])

                    # Move both pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second element (left pointer)
                    while left <right and n[left]==n[left-1]:
                        left =left+1
                    
                    # Skip duplicates for the third element (right pointer)
                    while left< right and n[right]== n[right+1]:
                        right=right-1 


                    
                
                elif cur_sum > target:
                    right=right-1
                else:
                    left=left +1

        print(res)

        return res
        

                
                



