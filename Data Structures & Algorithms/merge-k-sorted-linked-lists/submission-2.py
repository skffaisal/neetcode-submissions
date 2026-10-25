# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        if len(lists)<=1:
            return lists[0]

        mid=len(lists)//2

        left_portion=self.mergeKLists(lists[:mid])
        right_portion=self.mergeKLists(lists[mid:])

        return self.merge_2_Lists(left_portion,right_portion)




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
