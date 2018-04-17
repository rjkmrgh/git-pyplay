from StackQueue.Queue import Queue

class Stack(object):

    def __init__(self):
        self.qu1 = Queue()
        self.qu2 = Queue()

        
    def push(self, data):
         self.qu1.Enqueue(data)


    def pop(self):
        while self.qu1.head != self.qu1.tail-1:
            x = self.qu1.Dequeue()
            self.qu2.Enqueue(x)

        data = self.qu1.Dequeue()
        
        while self.qu2.head != self.qu2.tail:
            x = self.qu2.Dequeue()
            self.qu1.Enqueue(x)

        return data


    def traversal(self):
        self.qu1.traversal()