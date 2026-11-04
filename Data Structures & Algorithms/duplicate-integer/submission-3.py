class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pool=set()

        for ele in nums:
            if ele in pool:
                return True
            else:
                pool.add(ele)
        return False