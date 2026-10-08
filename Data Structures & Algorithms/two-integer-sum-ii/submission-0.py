class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:

        left =0
        right =len(n)-1

        while left < right:

            cur_sum=n[left]+n[right]

            if cur_sum == target:
                return [left+1,right+1] # 1-indexed
            
            if cur_sum > target:
                right=right-1
            else:
                left=left+1
        return []
        