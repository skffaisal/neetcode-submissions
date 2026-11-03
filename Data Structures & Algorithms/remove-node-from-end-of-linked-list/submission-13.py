# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow=ListNode(0,head)
        fast=slow

        save=slow

        index =0
        while n:
            fast=fast.next
            n=n-1
 

        while fast.next:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return save.next