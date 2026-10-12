class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0

        pool=set()

        max_length=0

        for right in range (len(s)):

            while s[right] in pool:
                pool.discard(s[left])
                left=left+1

            if s[right] not in pool:
                pool.add(s[right])
            
            max_length=max(max_length, right-left+1)

        return max_length

            

