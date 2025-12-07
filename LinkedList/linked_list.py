class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node 

        else:
            self.tail.next = new_node #previous last element of l_l will have next pointing to new node
            self.tail = new_node # now tail will actually contain the new node
        self.length+=1 

    def pop(self):
        if self.length==0: 
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        self.length-=1

        if self.length==0:  #this has to be done because after decrementing the length
            self.head = None
            self.tail=None
        return temp.value #returns which element we removed!
    

    def prepend(self,value):
        new_node = Node(value)

        if self.length==0:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1 
        return True


    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None

        self.length -= 1
        if self.length == 0:#after decrementing length!!
            self.tail = None
        return temp
    def get(self,index):
        if index < 0 or index >= self.length: #if the index is valid
            return None
        else:
            temp = self.head

            while(index>0):
                temp = temp.next
                index-=1
            return temp
            
    def set_value(self,index,value): #we will change the value of the index
        if index < 0 or index >= self.length: # validate index first
            return False

        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        
        if index==0:
            return self.prepend(value)
        
        if index==self.length:
            return self.append(value)
        
        new_node = Node(value)
        prev = self.get(index-1)
        if prev is None:
            return False

        new_node.next = prev.next
        prev.next = new_node

        self.length+=1
    def remove(self,index):
        if self.length == 0 or index < 0 or index >= self.length:
            return None
        
        if index == 0:
            node = self.pop_first()
            return node.value if node else None
        
        if self.length - 1 == index:
            return self.pop()
        
        prev = self.get(index-1)
        if prev is None or prev.next is None:
            return None
        temp = prev.next

        prev.next = temp.next

        temp.next = None

        self.length-=1
    def reverse(self):

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

            after = temp.next
            temp.next = before
            before = temp
            temp = after

            self.length-=1


             
    def display(self): 
        temp = self.head

        while temp is not None:
            print(temp.value,"\t")
            temp = temp.next


my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.prepend(100)
my_linked_list.display()
my_linked_list.pop()
my_linked_list.display()
my_linked_list.pop_first()
my_linked_list.display()
res = my_linked_list.get(0)
print("the item is:",res.value)
res=my_linked_list.insert(2,0)
print(res)