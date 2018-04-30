from AddOne.LinkedList import LinkedList

linkedlist = LinkedList()

linkedlist.insert_at_end(2)
linkedlist.insert_at_end(1)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)
linkedlist.insert_at_end(9)

linkedlist.traversal()

#reverse before add one
linkedlist.reverse()

#add one to end
linkedlist.add_one_at_begin()

#reverse after add one
linkedlist.reverse()

linkedlist.traversal()




