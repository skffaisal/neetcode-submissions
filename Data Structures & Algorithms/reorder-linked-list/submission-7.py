# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        save = head

        head2=slow.next
        slow.next= None

        prev=None
        curr=head2
        while curr:
            temp=curr.next
            curr.next=prev

            prev=curr
            curr=temp
        
        head2 = prev

        while head and head2:
            temp1 = head.next
            temp2= head2.next

            head.next=head2
            head2.next=temp1

            head=temp1
            head2=temp2
        head=save


