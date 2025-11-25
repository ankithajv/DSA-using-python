class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1

    def is_empty(self):
        return self.length == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp  # returns Node; use .value when printing

    def peek(self):
        return None if self.is_empty() else self.head.value

    def __len__(self):
        return self.length

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue contents:")
    q.print_queue()

    print("Peek:", q.peek())

    deq = q.dequeue()
    print("Dequeued:", deq.value if deq else None)

    print("After dequeue:")
    q.print_queue()
