from AddOne.Node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):

        curr = self.head
        node = Node(data)
        if curr is None:
            self.head = node
        else:
            while curr.next:
                curr = curr.next

            curr.next = node


    def reverse(self):

        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    def add_one_at_begin(self):

        curr = self.head
        prev = None
        while curr:

            if curr.data != 9:
                curr.data += 1
                curr = curr.next
                break
            else:
                curr.data  = 0
                prev = curr
                curr = curr.next
                if curr is None:
                    node = Node(1)
                    prev.next = node
                    break

    def traversal(self):

        curr = self.head
        s = ''
        while curr:
            s += str(curr.data)
            curr = curr.next

        print(s)
