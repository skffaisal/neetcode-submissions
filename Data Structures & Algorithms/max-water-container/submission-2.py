class Solution:
    def maxArea(self, n: List[int]) -> int:
        
        max_area=0

        left=0

        right=len(n)-1

        while left <right:

            area = (right-left) * (min(n[left],n[right]))

            if max_area < area:
                max_area=area
            
            if n[left] < n[right]:
                left += 1
            else:
                right -= 1

        return max_area





