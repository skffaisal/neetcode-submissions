# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head #p1 head of the first half list 

        # find the middle 
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # print(slow.val)

        # p2, head of the second half list 
        p2=slow.next # middle also in the second half
        slow.next=None # separate first half and second half
        


        # reverse the second half
        prev= None
        curr= p2

        while curr:
            temp=curr.next
            curr.next=prev

            prev=curr
            curr=temp

        p2=prev

        # while p1:
        #     print(p1.val)
        #     p1=p1.next

        while p1 and p2:
            temp1=p1.next
            p1.next=p2
            p1=temp1

            temp2=p2.next
            p2.next=p1
            p2=temp2

        # while head:
        #     print(head.val)
        #     head=head.next
        

        


