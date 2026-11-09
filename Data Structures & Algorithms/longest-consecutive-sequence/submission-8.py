class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool=set(nums)
        max_count=0
        for ele in pool:
            if ele-1 not in pool:
                count=1
                while ele+1 in pool:
                    count+=1
                    ele+=1
                max_count=max(max_count,count)
        return max_count