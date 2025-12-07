#This code check whether the linked list has a loop

#  10 -- 20
#  |      |
#  |      |
#  40 -- 30


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
            new_node.next = self.head  #THIS WILL CREATE A LOOP IN LINKED LIST

        return True

    def has_loop(self):

        slow = self.head
        fast = self.head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
print(my_linked_list_1.has_loop()) # Returns True   

        
    
    