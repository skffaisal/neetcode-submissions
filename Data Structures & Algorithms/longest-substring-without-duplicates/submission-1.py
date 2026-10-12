class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0

        pool=set()

        max_length=0

        for right in range (len(s)):

            while s[right] in pool: # when same character is encountered
                pool.discard(s[left])
                left=left+1

            pool.add(s[right])
            
            max_length=max(max_length, right-left+1)

        return max_length

            

