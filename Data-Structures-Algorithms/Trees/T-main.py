'''

(2^n) - 1 where n denotes how many levels of the tree there are --> O(logn)
If a tree never forks, it's a linked list - worst case scenario in terms of time → O(n)
Perfect tree Give the best time scenarios

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True

        temp = self.root
        
        while (True):
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value: # check leftside
                if temp.left is None: # if no node is there, then insert
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left

            else: # check rightside
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        # -- actually not needed as it'll return false anyways since temp will be None
        # if self.root == None:
        #     return False
        
        temp = self.root
        while temp is not None:
            if value < temp.value:
                 temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

            
            

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print("contains...20?")
print(my_tree.contains(20))
print("contains...1?")
print(my_tree.contains(1))
print("min node from root")
print(my_tree.min_value_node(my_tree.root).value)