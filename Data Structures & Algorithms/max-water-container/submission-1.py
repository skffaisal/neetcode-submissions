class Solution:
    def maxArea(self, n: List[int]) -> int:
        
        # need to find length X width for the area

        # select the two bars , such that the width should be max

        max_1=0
        max_2=0

        max_area=0

        for i in range(len(n)):
            if max_1<n[i]:
                max_2=max_1
                max_1=n[i]
            elif n[i]!= max_1 and max_2<n[i]:
                max_2=n[i]
        
        print(max_1, max_2)

        seen=set()
        seen.add(max_1)
        seen.add(max_2)

        left=0

        right=len(n)-1

        while left <right:

            # while left<right and n[left] not in seen:
            #     left=left+1

            # while left<right and n[right] not in seen:
            #     right=right-1


            area = (right-left) * (min(n[left],n[right]))

            if max_area < area:
                max_area=area
            
            if n[left] < n[right]:
                left += 1
            else:
                right -= 1

        return max_area





