class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()

        res=[]

        for i in range(len(n)):

            if i>0 and n[i]==n[i-1]:
                continue
            target = -n[i]
            l=i+1
            r=len(n)-1

            while l<r:

                cur_sum = n[l]+n[r]

                if cur_sum == target:
                    
                    res.append([n[l],n[r],n[i]])

                    
                    l=l+1
                    r=r-1

                    while l<r and n[l]==n[l-1]:
                        l=l+1
                    while l<r and n[r]==n[r+1]:
                        r=r-1
                elif cur_sum > target:
                    r=r-1
                else:
                    l=l+1
        return res
            