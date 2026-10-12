class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        pool=set()

        max_len=0

        for r in range(len(s)):
            
            # add if not in pool
            if s[r] not in pool:
                pool.add(s[r])
                max_len=max(max_len,r-l+1)
                continue

            while s[r] in pool:
                pool.discard(s[l])
                l+=1
            
            pool.add(s[r])

            max_len=max(max_len,r-l+1)
        return max_len


