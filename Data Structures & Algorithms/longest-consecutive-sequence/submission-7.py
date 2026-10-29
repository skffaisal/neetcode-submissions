class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        pool=set(n)
        max_count=0

        for i in range(len(n)):
            if n[i]-1 not in pool: #start of the sequence
                count=1
                ele=n[i]+1
                while ele in pool:
                    count+=1
                    ele+=1
                max_count=max(max_count,count)
        return max_count
                