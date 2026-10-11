class Solution:
    def longestConsecutive(self, n: List[int]) -> int:

        pool= set (n)

        diff=0

        for ele in pool:

            if ele-1 not in pool:

                count=1
                next_seq=ele+1

                while next_seq in pool:
                    count+=1
                    next_seq+=1

                diff = max(diff,count)

        return diff
                
        