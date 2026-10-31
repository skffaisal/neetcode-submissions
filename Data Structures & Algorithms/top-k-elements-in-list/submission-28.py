class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        f={}

        for i in range(len(n)):
            f[n[i]]=f.get(n[i],0)+1
        # print(f)

        buckets=[[] for _ in range(max(f.values())+1)]

        # print(buckets)

        for value,frequency in f.items():
            buckets[frequency].append(value)
        # print(buckets)
        res=[]
        for i in range(len(buckets)-1,-1,-1):
            for vals in buckets[i]:
                res.append(vals)
                if len(res)==k:
                    return res
        # print(res)
