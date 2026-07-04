"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return None

        temp = head
        while temp:
            newnode = Node(temp.val)
            newnode.next = temp.next
            temp.next = newnode
            temp = newnode.next
        
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        
        dummynode = Node(0)
        clone = dummynode
        temp = head
        while temp:
            clone.next = temp.next
            temp.next = temp.next.next
            temp = temp.next
            clone = clone.next
        
        return dummynode.next

