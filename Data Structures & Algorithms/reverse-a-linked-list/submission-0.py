# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#iterative approach
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         previous = None
#         current = head
#         while current:
#             nxt = current.next #store next node
#             current.next = previous #reverse current node pointer
#             previous = current #move prev to current
#             current = nxt #move cur to next node
#         return previous 

#refactor/recursive approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head #reverses link from head and original next
        head.next = None #breaks original link
        return new_head    