# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # usng dubby node, you dont have to worry about two things
        # 1. slow pointer pointing to the node before the target node
        # 2. the head node being removed, 

        dummy=ListNode(next=head)

        slow=dummy # so its like one before offset
        fast =head

        count=0

        while count<n:
            fast=fast.next
            count+=1

        while fast:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next
        return dummy.next
