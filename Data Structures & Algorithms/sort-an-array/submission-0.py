class Solution:
    def sortArray(self, n: List[int]) -> List[int]:
        # implimenting merge sort

        if len(n)<=1:
            return n
        
        mid=len(n)//2

        left=n[:mid]
        right=n[mid:]

        left = self.sortArray(left)
        right = self.sortArray (right)

        return self.merge(left,right)

    
    def merge(self,left:list[int],right:list[int])->list[int]:

        i=0
        j=0
        result=[]

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

obj= Solution()
print(obj.merge([1,3],[2,4]))
        