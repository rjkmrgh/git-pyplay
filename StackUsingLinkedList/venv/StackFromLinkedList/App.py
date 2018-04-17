from StackFromLinkedList.Stack import Stack

st = Stack()

st.push(20)
st.push(31)
st.push(42)
st.push(51)
st.push(63)

st.traversal()

print('Popped {}'.format(st.pop()))

st.traversal()