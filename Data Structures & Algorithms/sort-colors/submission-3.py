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
        # print(count)

        # if stable count needed 

        for i in range(1,len(count)):
            count[i]=count[i-1]+count[i]
        # print(count)

        output=[0]* len(n)

        # right to left
        for i in range(len(n)-1,-1,-1):
            value=n[i]
            position=count[value]-1
            output[position]=value
            count[value]-=1
        for i in range(len(n)):
            n[i]=output[i]




