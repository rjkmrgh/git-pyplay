from StackFromLinkedList.LinkedList import LinkedList


class Stack(object):

    def __init__(self):
        self.ll = LinkedList()
        self.top = 0


    def push(self, data):
        self.ll.insert(data)
        self.top = self.top +1


    def pop(self):
        data = self.ll.delete()
        self.top = self.top - 1
        return data


    def traversal(self):
        self.ll.traversal()