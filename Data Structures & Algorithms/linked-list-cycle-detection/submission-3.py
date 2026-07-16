# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and slow:
            if slow.next:
                slow = slow.next
            else:
                return False
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False

            if slow == fast:
                return True

        return False
            
