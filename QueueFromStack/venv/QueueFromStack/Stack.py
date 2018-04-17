
class Stack(object):

    def __init__(self):
        self.top = -1
        self.length = 10
        self.storage = [float('-inf')] * self.length


    def stack_empty(self):

        if self.top == -1:
            return True
        return False


    def push(self, data):

        if self.top != self.length:
            self.top += 1
            self.storage[self.top] = data
        else:
            print('Stack Overflow')

    def pop(self):

        if self.stack_empty():
            print('Stack Underflow')
        else:
            data = self.storage[self.top]
            self.top -= 1
            return data

    def traversal(self):

        if self.stack_empty():
            print('Stack is empty')
        else:
            print(self.storage)