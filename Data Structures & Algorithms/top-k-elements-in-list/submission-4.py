class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        
        freq={}

        for i in range (len(n)):
            freq[n[i]]=freq.get(n[i],0)+1
        # print(freq)

        buckets=[[] for _ in range(max(freq.values())+1)]

        # print(buckets)

        for value, frequency in freq.items():
            buckets[frequency].append(value)

        # print(buckets)

        res=[]
        for frequency in range(len(buckets)-1,-1,-1):
            for value in buckets[frequency]:
                res.append(value)
                if len(res)==k:
                    break
                # print(value)
            if len(res)==k:
                break
        print(res)
        return res
            

        
        