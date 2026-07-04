# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = l1, l2
        carry = 0

        dummynode = ListNode(0)
        temp = dummynode

        while temp1 or temp2 or carry:
            sum = carry

            if temp1:
                sum += temp1.val
                temp1 = temp1.next
            if temp2:
                sum += temp2.val
                temp2 = temp2.next

            newnode = ListNode(sum % 10)
            temp.next = newnode
            temp = temp.next
            carry = sum // 10

        return dummynode.next