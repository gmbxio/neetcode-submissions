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

        oldNewMap = {}
        temp = head

        while temp:
            newNode = Node(temp.val)
            oldNewMap[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            clone = oldNewMap[temp]
            clone.next = oldNewMap.get(temp.next)
            clone.random = oldNewMap.get(temp.random)
            temp = temp.next

        return oldNewMap[head]