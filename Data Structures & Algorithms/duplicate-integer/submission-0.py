class Solution:
    def hasDuplicate(self, n: List[int]) -> bool:
        seen=set()
        for i in range (len(n)):
            if n[i] in seen:
                return True
            else:
                seen.add(n[i])
        return False