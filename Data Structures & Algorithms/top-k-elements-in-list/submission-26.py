class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        res =[]
        freq={}
        for i in range(len(n)):
            freq[n[i]]=freq.get(n[i],0)+1
        
        buckets = [[] for _ in range (max(freq.values())+1)]

        # print(buckets)

        for value, frequency in freq.items():
            buckets[frequency].append(value)
        
        # print(buckets)

        for i in range (len(buckets)-1,-1,-1):
            for ele in buckets[i]:
                res.append(ele)
                if len(res)==k:
                    return res
      
        