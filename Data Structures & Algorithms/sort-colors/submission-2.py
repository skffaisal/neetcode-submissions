class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort 

        max_ele=max(n)

        count =[0]* (max_ele+1)

        # need to map values with indexes
        for i in range(len(n)):
            count[n[i]]+=1

        # now putting back in the order
        write_index=0

        for i in range(len(count)):
            freq=count[i]
            value=i # ie index only, no normalisation was done
            while(freq):
                n[write_index]= value
                write_index+=1
                freq-=1

        print(count)



