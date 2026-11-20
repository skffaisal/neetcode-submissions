class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        my_set=set(n)
        max_count =0
        for ele in my_set:
            if ele-1 not in my_set:
                count=1
                while ele+1 in my_set:
                    count+=1
                    ele+=1
                max_count=max(max_count,count)
        return max_count