import heapq
class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        
        freq={}

        for i in range (len(n)):
            freq[n[i]]=freq.get(n[i],0)+1

        # print(freq)

        heap=[]
        
        for value, frequency in freq.items(): # this loop automatically maintains the top k elements
            heapq.heappush(heap,(frequency,value))# reversing it, becasue the tuples first value is compared here
            
            if (len(heap)>k):
                heapq.heappop(heap)
        

        # print(heap)

        res=[]
        for frequency,value in heap:
            res.append(value)

        return res



