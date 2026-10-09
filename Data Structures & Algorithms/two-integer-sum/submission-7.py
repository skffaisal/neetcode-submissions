class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        new_list=[]
        # grouping indexes with elements to sort 
        for i in range(len(n)):
            new_list.append((n[i],i)) # ie creting tuples

        # print(new_list)

        # now sorting , to use 2 pointers

        new_list.sort()

        # print(new_list)

        left=0
        right=len(new_list)-1

        while left<right:

            cur_sum= new_list[left][0]+new_list[right][0]
        

            if cur_sum == target:
                return [min(new_list[left][1], new_list[right][1]), # just for the order of the output indexes
                        max((new_list[left][1], new_list[right][1]))]
                # print(min(new_list[left][1], new_list[right][1]),
                #         max((new_list[left][1], new_list[right][1])))

            if cur_sum > target:
                right=right-1
            else:
                left=left+1
        return []