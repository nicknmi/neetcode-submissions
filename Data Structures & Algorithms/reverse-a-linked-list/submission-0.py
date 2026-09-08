# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # len 0
        if not head:
            return None

        prev = None
        current = head

        while current != None:
            future = current.next
            
            current.next = prev
            prev = current

            current = future
        
        return prev