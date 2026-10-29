class Solution:
    def hasDuplicate(self, n: List[int]) -> bool:
        
        pool=set()

        for i in range(len(n)):
            if n[i] in pool:
                return True
            pool.add(n[i])
        return False