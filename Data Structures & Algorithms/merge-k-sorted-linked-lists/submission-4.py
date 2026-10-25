# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # O(NLogK)
        
        return self._merge_range(lists, 0, len(lists) - 1)

    def _merge_range(self, lists, start, end):
        if start > end:
            return None

        if start == end:
            return lists[start]

        mid = (start + end) // 2

        left = self._merge_range(lists, start, mid)
        right = self._merge_range(lists, mid + 1, end)

        return self.merge_2_Lists(left, right)


    def merge_2_Lists(slef, left, right)-> Optional[ListNode]:

        if not left:
            return right

        if not right:
            return left

        d=ListNode()
        head=d


        while left and right:

            if left.val<=right.val:
                d.next=left
                left=left.next
            else:
                d.next=right
                right=right.next
            d=d.next
        
        if left:
            d.next=left
        if right:
            d.next=right


        return head.next
