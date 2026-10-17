class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        
        n=sorted(n)

        print(n)


        res=[]

        for i in range(len(n)):

            if i>0 and n[i]==n[i-1]:
                continue 

            target=-n[i] # a+b=-c

            l=i+1
            r=len(n)-1

            while l < r:

                if n[l]+n[r]==target:
                    res.append([n[l],n[r],n[i]])
                    l=l+1
                    r=r-1

                    while l<r and n[l]==n[l-1]:
                        l=l+1
                    while l<r and n[r] ==n[r+1]:
                        r=r-1

                if n[l]+n[r] > target:
                    r-=1
                if n[l]+n[r] < target:
                    l+=1

                
        print (res)
        return (res)


                