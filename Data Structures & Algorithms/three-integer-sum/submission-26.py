class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        res=[]
        for i in range(len(n)):
           
            if i>0 and n[i]==n[i-1]:
                continue

            l=i+1
            r=len(n)-1

            # a=-(b+c)
            target=-n[i]
            while l<r:
                curr_sum=n[l]+n[r]

                if curr_sum == target:
                    res.append([n[i],n[l],n[r]])

                    l=l+1
                    while l<r and n[l]==n[l-1]:
                        l=l+1
                    r=r-1
                    
                    while l<r and n[r]==n[r+1]:
                        r=r-1
    
                elif l<r and curr_sum>target:
                    r=r-1
                elif l<r and curr_sum<target :
                    l=l+1
        return (res)
                
