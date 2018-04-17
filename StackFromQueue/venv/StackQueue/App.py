from StackQueue.Stack import Stack

st = Stack()

st.push(20)
st.push(34)
st.push(47)
st.push(76)

st.traversal()

print('poped {}'.format( st.pop()))

st.traversal()