# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 =list(), list()
        while l1 is not None:
            num1.insert(0, l1.val)
            l1 = l1.next
        
        while l2 is not None:
            num2.insert(0, l2.val)
            l2 = l2.next
            
        temp = int(''.join(map(str,num1))) + int(''.join(map(str,num2)))
        result = None
        
        for i in map(int,str(temp)):
            result = ListNode(val=i, next=result)
            
        return result