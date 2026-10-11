class Solution:
    def longestConsecutive(self, n: List[int]) -> int:

        pool= set (n)

        diff=0

        for i in range(len(n)):

            # if previosu element is not there , thats the start of the sequence

            if n[i]-1 not in pool:
                cum_sum=1
                ele=n[i]
                while ele+1 in pool:
                    cum_sum+=1
                    ele+=1
                
                diff=max(cum_sum,diff)

        return diff
        