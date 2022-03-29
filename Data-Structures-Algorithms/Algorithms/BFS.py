# start at top - go by level - row by row
# storing entire node (including its left, right) in the queue

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

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node) # entire node

        while len(queue) > 0: # run until queue is empty
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None: # if there is a left node
                queue.append(current_node.left)
            if current_node.right is not None: # if there is a right node
                queue.append(current_node.right)

        return results
            

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.BFS()) # [47, 21, 76, 18, 27, 52, 82]

