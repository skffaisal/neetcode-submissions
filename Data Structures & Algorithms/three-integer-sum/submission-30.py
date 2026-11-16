class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        res=[]
        for i in range (len(n)):
            
            if i>0 and n[i]==n[i-1]:
                continue

            a= n[i]
            l=i+1
            r=len(n)-1
            target=-(a)

            while l<r:
                cum_sum=n[l]+n[r]

                if target==cum_sum:
                    res.append([n[i],n[l],n[r]])
                    l=l+1
                    while l<r and  n[l]==n[l-1]:
                        l=l+1

                    r=r-1
                    while l<r and n[r]==n[r+1]:
                        r=r-1
                elif target< cum_sum:
                    r=r-1
                else:
                    l=l+1
        return (res)
                
