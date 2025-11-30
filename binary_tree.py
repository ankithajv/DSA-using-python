class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,value):

        newnode = Node(value)

        if self.root == None:
            self.root = newnode
            return True

        temp = self.root
        while 1:
            #checks if there is identical value
            if newnode.value == temp.value:
                return False
            
            if newnode.value < temp. value:
                if temp.left == None:
                    temp.left = newnode
                    return True
                
                temp = temp.left

            else:
                if temp.right == None:
                    temp.right = newnode
                    return True
                
                temp = temp.right

        
    def contains(self,value):
        temp = self.root
        while (temp is not None):

            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right

            else:
                return True
            
        
        return False
        

my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(20)
my_tree.insert(30)

print(my_tree.contains(30))





            





                             