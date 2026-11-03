# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2lists(l1,l2):
            if not l1:
                return l2
            if not l2:
                return l1

            d= ListNode()
            p=d

            while l1 and l2:
                if l1.val<=l2.val:
                    p.next=l1
                    l1=l1.next
                else:
                    p.next=l2
                    l2=l2.next
                p=p.next
            
            if l1:
                p.next=l1
            if l2:
                p.next=l2
            return d.next

        if not lists:
            return None
        if len(lists)<=1:
            return lists[0]
            
        m=len(lists)//2

        left= self.mergeKLists(lists[:m])
        right=self.mergeKLists(lists[m:])

         
        return merge2lists(left,right)
