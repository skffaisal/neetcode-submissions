class Solution:
    def longestConsecutive(self, n: list[int]) -> int:

        my_set=set(n)
        # print(my_set)

        

        max_count=0

        for num in my_set:

            if (num-1 ) not in my_set: # ie if no previous elemet is present, it s the start of the sequence

                count=1 # ie couting it as a first elemets regardless if consequtives elements are there or not 
                
                next_seq=num +1 
                
                # keep going till the sequence finishes 
                while next_seq in my_set:
                    count+=1
                    next_seq+=1

                #update the max count of each sequence
                if max_count < count:
                    max_count = count

        return max_count







                


        