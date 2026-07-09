# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        temp = head

        while temp:
            nextNode = temp.next
            temp.next = prevNode

            prevNode = temp
            temp = nextNode
        
        return prevNode

    def getKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        k -= 1

        while temp and k > 0:
            temp = temp.next
            k -= 1
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = None

        while temp:
            kthNode = self.getKthNode(temp, k)

            if not kthNode:
                if prevNode:
                    prevNode.next = temp
                break
            
            nextNode = kthNode.next
            kthNode.next = None

            self.reverseList(temp)

            if temp == head:
                head = kthNode

            else:
                prevNode.next = kthNode
                
            prevNode = temp
            temp = nextNode


        return head