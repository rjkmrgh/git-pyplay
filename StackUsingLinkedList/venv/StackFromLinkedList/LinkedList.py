from StackFromLinkedList.Node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0


    def insert(self, data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head

        self.head = node


    def delete(self):
        if self.head is not None:
            x = self.head
            data = x.data
            self.head = self.head.next
            del x.data
            del x.next
        return data


    def traversal(self):
        curr = self.head
        print('Linkedlist traversal..')
        while curr is not None:
            print(curr.data)
            curr = curr.next