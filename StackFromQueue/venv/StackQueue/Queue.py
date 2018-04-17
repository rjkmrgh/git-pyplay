
class Queue(object):


    def __init__(self):
        self.length = 10
        self.queue = [None] * self.length
        self.head = -1
        self.tail = 0


    def Enqueue(self, data):
        if self.tail == self.length:
            #print('Overflow')
            self.tail = 0

        if self.head == -1:
            self.head = 0

        self.queue[self.tail] = data
        self.tail += 1


    def Dequeue(self):

        if self.head == self.length:
            #print('Underflow')
            self.head = 0
        x = self.queue[self.head]
        self.head += 1
        return x


    def traversal(self):
        for i in range(self.head, self.tail):
            print(self.queue[i])
