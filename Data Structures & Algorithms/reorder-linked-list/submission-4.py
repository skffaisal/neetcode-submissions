# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head 

        slow=head
        fast=head.next # this also gives the same result

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        p2=slow.next
        slow.next=None 

        prev= None
        curr= p2

        while curr:
            temp=curr.next
            curr.next=prev

            prev=curr
            curr=temp

        p2=prev


        while p1 and p2:
            temp1=p1.next
            temp2=p2.next

            p1.next=p2
            p2.next=temp1
            
            p1=temp1
            p2=temp2

        


