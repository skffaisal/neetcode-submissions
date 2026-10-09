class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        # using hash map

        # a+b+c=0
        # c=-(a+b)

        res=set()

        for i in range (len(n)):
            a=n[i]
            seen=set() # becasue i dont want the index like two sum, i just want to check if that value appeared
            for j in range(i+1,len(n)): # i+1, becase if not, same triplet with another combination will result
                
                b=n[j]

                target = -(n[i]+n[j])

                if target in seen:
                    res.add(tuple(sorted([a,b,target])))
                
                seen.add(n[j])

        # print(res)
        return [list(ele) for ele in res]




