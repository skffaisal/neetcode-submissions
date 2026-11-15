class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        f={}

        res=[]

        for i in range(len(n)):
            f[n[i]]=f.get(n[i],0)+1
        # print(f)
        
        buckets=[[] for _ in range(max(f.values())+1)]
        # print(buckets)

        for val,freq in f.items():
            buckets[freq].append(val)
        # print(buckets)
        
        for i in range (len(buckets)-1,-1,-1):
            for val in buckets[i]:
                res.append(val)
                if len(res)==k:
                    return res

            