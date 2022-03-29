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


    # Depth First Search
    ''' Tree --
            47
        21      76
    18  27      52  82
    '''

    # PreOrder --> 47,21,18,27,76,52,82
    # PostOrder --> Write value after its gone left and right-->  18,27,21, 52,82,47
    # InOrder --> similar to Postorder but it goes left write right  --> 18,21,27,47,52,76,82
    
    def dfs_preorder(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_postorder(self): # same code as preorder just append is at the end
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
    def dfs_inorder(self): # same code as preorder just append is in the middle
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
            
        
        traverse(self.root)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("DFS - Preorder")
print(my_tree.dfs_preorder())
print("DFS - Postorder")
print(my_tree.dfs_postorder())
print("DFS - InOrder")
print(my_tree.dfs_inorder())