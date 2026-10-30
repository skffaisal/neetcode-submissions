class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        d={}

        for i in range(len(n)):
            if target - n[i] in d:
                
                return [d[target - n[i]],i] 
            d[n[i]]=i