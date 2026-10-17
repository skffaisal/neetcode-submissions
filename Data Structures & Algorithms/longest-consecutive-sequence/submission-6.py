class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        
        my_set=set(n)
        max_count=0
        for i in range(len(n)):
            
            if n[i]-1 not in my_set:
                count=1
                next_ele = n[i]+1
                while next_ele in my_set:
                    count+=1
                    next_ele+=1
                max_count=max(max_count,count)
        return max_count
