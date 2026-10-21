# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #want to compare each node you see to every node you have seen.
        #if you see the same one twice, you're in a cycle. 
        seen = []
        current = head
        while True:
            if current is None:
                return False
            current = current.next 
            if current in seen:
                return True
            seen.append(current)






        