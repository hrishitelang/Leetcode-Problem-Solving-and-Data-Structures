class Node(object):
    def __init__(self, data):
        self.data = data ##
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def insertstart(self, data):
        newNode = Node(data) ##
        self.size += 1
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode ##

    def remove(self, data): ##
        if self.head is None:
            return
        node = self.head
        previous_node = None
        self.size -= 1
        while node.data != data:
            previous_node = node
            node = node.next

        if previous_node is None:
            self.head = node.next;
        else:
            previous_node.next = node.next;

    def size(self):
        return self.size

    def size2(self):
        size = 0
        temp = self.head
        while temp.next is not None:
            size += 1
            temp = temp.next
        return size

    def insertend(self, data):
        new_node = Node(data)
        temp = self.head
        self.size += 1
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp is not None: ##
            print(f"{temp.data}")
            temp = temp.next

l = LinkedList()
l.insertstart(12)
l.insertstart(13)
l.insertstart(1)
l.insertend(19)
l.traverse()
l.remove(13)
print('\n')
l.traverse()
