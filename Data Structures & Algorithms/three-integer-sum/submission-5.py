class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        # keep one fixed, find the other 2 using two sum technique
        # pointer approach
        
        n.sort()

        res=[]

        for i in range(len(n)):
            target= -(n[i])

            left=i+1
            right=len(n)-1

            while left < right and left!=i and right!=i: # no pointers should point to the current frozen element 

                cur_sum= n[left]+n[right]

                if cur_sum == target:
                    if [n[i],n[left],n[right]] not in res:
                        res.append([n[i],n[left],n[right]])
                
                if cur_sum > target:
                    right=right-1
                else:
                    left=left +1

        # print(res)

        return res
        

                
                



