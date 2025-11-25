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

if __name__ == "__main__":
    # simple main to demonstrate Stack usage
    s = Stack(10)
    s.push(20)
    s.push(30)

    print("Stack contents:")
    s.print_stack()

    print("Peek:", s.peek())

    popped = s.pop()
    print("Popped:", popped.value if popped else None)

    print("After pop:")
    s.print_stack() 
