#Without length constraint

class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        return True
    
    def middle_node(self):

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
    
l_list = LinkedList(2)

l_list.append(3)
l_list.append(4)
l_list.append(5)
l_list.append(6)
l_list.append(7)
res = l_list.middle_node()
print(res)







