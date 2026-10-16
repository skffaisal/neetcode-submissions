from typing import List

class Solution:
    def search(self, n: List[int], target: int) -> int:
        if not n:
            return -1
            
        l = 0
        r = len(n) - 1

        # Step 1: Find the index of the smallest element (pivot)
        while l < r: 
            m = (l + r) // 2
            if n[m] > n[r]:
                l = m + 1
            else:
                r = m

        min_index = l

        # Step 2: Determine which sorted subarray contains the target
        # Reset both l and r explicitly for the chosen half
        if target >= n[min_index] and target <= n[-1]:
            l = min_index
            r = len(n) - 1
        else:
            l = 0
            r = min_index - 1

        # Step 3: Standard binary search on the chosen half
        while l <= r:
            m = (l + r) // 2
            if target == n[m]:
                return m
            elif target > n[m]:
                l = m + 1
            else:
                r = m - 1
                
        return -1
