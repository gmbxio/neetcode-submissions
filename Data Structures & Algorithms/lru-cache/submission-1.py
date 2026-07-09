class Node:

    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodemap = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail 
        self.tail.prev = self.head

    def deleteNode(self, node: Node):
        nextNode = node.next
        prevNode = node.prev

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addToHead(self, node: Node):
        nextNode = self.head.next

        self.head.next = node
        node.next = nextNode

        nextNode.prev = node
        node.prev = self.head


    def get(self, key: int) -> int:
        if key in self.nodemap:
            node = self.nodemap[key]

            self.deleteNode(node)
            self.addToHead(node)

            return node.val

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.nodemap:
            node = self.nodemap[key]

            node.val = value
            self.deleteNode(node)
            self.addToHead(node)
        
        else:
            newnode = Node(key, value)
            self.nodemap[key] = newnode
            self.addToHead(newnode)

            if len(self.nodemap) > self.capacity:
                prevnode = self.tail.prev
                self.deleteNode(prevnode)
                del self.nodemap[prevnode.key]
