# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length=0

        p=head
        while (p):
            length+=1
            p=p.next
        print(f"length of the list is {length}")

        target=length-n

        p=head
        if target == 0:
            return p.next


        position =1 # not index based
        p=head
        while p:
            print(f"value is {p.val}, its index is {position}")

            if position ==target:
                break

            p=p.next
            position+=1

        print(p.val)

        p.next=p.next.next

        return head