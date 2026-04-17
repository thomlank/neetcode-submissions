# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None 
        prev = None
        curr = mid
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        reversed_half = prev
        original = head
        while reversed_half:
            tmp1 = original.next
            tmp2 = reversed_half.next
            original.next = reversed_half
            reversed_half.next = tmp1
            original = tmp1
            reversed_half = tmp2       
           