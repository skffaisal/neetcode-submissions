class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        
        count={}
        res=[]

        for i in range (len(n)):
            count[n[i]]=count.get(n[i],0)+1

        # print(count)

        buckets = [[] for _ in range(len(n)+1)]

        # print(buckets)

        for value,frequency in count.items():
            buckets[frequency].append(value)

        for i in range (len(buckets)-1,-1,-1):
            for value in buckets[i]:
                res.append(value)

                if len(res)==k:
                    return res


        