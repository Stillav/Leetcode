# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None 
        slow = head 
        
        while slow:
            next_, slow.next, rev = slow.next, rev, slow
            slow = next_
        
        return rev
            
        
            