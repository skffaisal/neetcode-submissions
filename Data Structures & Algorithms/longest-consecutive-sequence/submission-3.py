class Solution:
    def longestConsecutive(self, n: List[int]) -> int:

        pool =set(n)

        max_count=0

        for i in range (len(n)):
            if n[i] -1 not in pool: # means its the start of a sequence
                count =1 # ie counting this startelement
                j=1
                while (n[i] +j) in pool:
                    count+=1
                    j+=1

                if max_count < count:
                    max_count=count


        return max_count
                


        