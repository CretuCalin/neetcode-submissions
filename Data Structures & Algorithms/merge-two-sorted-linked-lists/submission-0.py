# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        
        curr = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1 != None:
            curr.next = list1
        elif list2 != None:
            curr.next = list2

        return head

# sol = Solution()

# list1  = ListNode(5)
# list1.next = ListNode(7)
# list1.next.next = ListNode(9)

# list2  = ListNode(6)
# list2.next = ListNode(8)
# list2.next.next = ListNode(10)
# list2.next.next.next = ListNode(14)

# list_final = sol.mergeTwoLists(list1, list2)

# curr = list_final

# while curr:
#     print(curr.val)
#     curr = curr.next

