# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, root: Optional[ListNode]) -> Optional[ListNode]:
        if not root:
            return None 
        if not root.next:
            return root
        new_head=self.reverseList(root.next)
        root.next.next=root
        root.next=None

        return new_head
        
