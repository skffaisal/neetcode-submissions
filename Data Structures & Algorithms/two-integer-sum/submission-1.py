class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:

        pool ={}

        for i in range(len(n)):
            if target-n[i] in pool:
                return [pool[target-n[i]],i]
            pool[n[i]]=i
        