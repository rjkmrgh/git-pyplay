from QueueFromStack.Stack import Stack
from QueueFromStack.Queue import Queue

st = Stack()
st1 = Stack()

q = Queue()

#st.push(19)
#st.push(2)
#st.push(36)
#st.push(94)
#st.push(68)
#st.traversal()
#print(st.pop())

q.enqueue(19)
q.enqueue(2)
q.enqueue(36)
q.enqueue(94)
q.enqueue(68)

print(q.dequeue())
print(q.dequeue())