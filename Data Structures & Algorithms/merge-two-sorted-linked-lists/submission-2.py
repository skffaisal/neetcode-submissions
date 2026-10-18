# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a 
        p1=list1
        p2=list2

        # edge case:
        if p1 is None: # ie the list is empty
            return p2

        if p2 is None:
            return p1


        head=None
        # creating a new node with min value 
        if p1.val<=p2.val:
            head=ListNode(p1.val)
            p1=p1.next
        else:
            head=ListNode(p2.val)
            p2=p2.next

        p=head

        while p1 and p2:
            
            if p1.val<=p2.val:
                # add p1.val to the new linked list
                new_node=ListNode(p1.val)
                p.next=new_node
                p=p.next
                p1=p1.next
            else:
                # add p2.val to the new linked list
                new_node=ListNode(p2.val)
                p.next=new_node
                p=p.next
                p2=p2.next

        # even after the comparision , if any elements remainig
        while p1 is not None:
            new_node=ListNode(p1.val)
            p.next=new_node
            p=p.next
            p1=p1.next

        while p2 is not None:
            new_node=ListNode(p2.val)
            p.next = new_node
            p=p.next
            p2=p2.next


        return head



