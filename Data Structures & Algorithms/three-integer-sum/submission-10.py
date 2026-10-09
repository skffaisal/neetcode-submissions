class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        # keep one fixed, find the other 2 using two sum technique
        # pointer approach
        
        n.sort() # helps avoid duplicates

        res=set()

        for i in range(len(n)):
            target= -(n[i])

            left=i+1
            right=len(n)-1

            while left < right:

                cur_sum= n[left]+n[right]

                if cur_sum == target:
                    
                    res.add((n[i],n[left],n[right]))
                    
                    left =left+1
                    right=right-1 # so that other pair also can be for if any for the current fixed n[i]
                    
                
                elif cur_sum > target:
                    right=right-1
                else:
                    left=left +1

        # print(res)

        res = [list(ele) for ele in res]

        return res
        

                
                



