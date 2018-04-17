from QueueFromStack.Stack import Stack

class Queue(object):

    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
        
    def enqueue(self, data):
        self.st1.push(data)
    
    def dequeue(self):
        
        if self.st2.stack_empty():
            while not self.st1.stack_empty():
                x = self.st1.pop()
                self.st2.push(x)

        return self.st2.pop()
