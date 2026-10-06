class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # going with selection sort

        for i in range (len(n)-1):
            min_index=i

            for j in range(i+1,len(n)):
               if n[j]<n[min_index]:
                min_index=j

            if min_index!=i:
                n[min_index],n[i]=n[i],n[min_index]


