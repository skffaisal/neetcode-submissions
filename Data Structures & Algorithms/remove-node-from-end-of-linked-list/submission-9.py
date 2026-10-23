class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast=head
        slow=head

        count=0
        while count<=n: # Move the first pointer n+1 steps ahead from the head. 

            if fast is None:
                # print("n==len(list)")
                return head.next

            fast=fast.next
            count+=1


    
        while fast: #start another pointer,and iterate both pointers simultaneously until first reaches null 
            slow=slow.next
            fast=fast.next

        # print(slow.val) # slow will poin to one node before the node to delete

        slow.next=slow.next.next

        return head































