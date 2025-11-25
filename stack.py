class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        if self.top is None:
            return None
        
        temp = self.top
        while self.top.next is not None:
            print(temp.value)
            temp = temp.next


    def push(self,value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length+=1

    def pop(self):

        if self.top is None:
            return None

        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length-=1
            return temp
        
    def peek(self):
        if self.top is None:
            return None
        
        else:
            return self.top.value
        

