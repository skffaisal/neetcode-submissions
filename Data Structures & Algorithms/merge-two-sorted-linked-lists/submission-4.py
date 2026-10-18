# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Optimal, using existing nodes

        p1=list1
        p2=list2

        # if either list is empty
        if p1 is None:
            return p2
        elif p2 is None:
            return p1

        if list1.val<=list2.val: # ie the head points to the list with the smaller starting node
            head=list1
            p1=p1.next # then move that list's pointer to next node, 
        else:
            head=list2
            p2=p2.next
        
        # basically in the above block, skipping the node which we considered as head

        # head will be returned , so need another variable for completing the merged list 

        p=head

        while p1 and p2: 
            if p1.val<=p2.val:
                p.next=p1
                p1=p1.next
            else:
                p.next=p2
                p2=p2.next

            p=p.next # merged list pointer, advances in either cases

        # handle if any extra nodes remaining in either lists
        if p1: # ie p1 is not None, meaning still one or more elements in pointer p1
            p.next=p1
        else:
            p.next=p2

        return head


