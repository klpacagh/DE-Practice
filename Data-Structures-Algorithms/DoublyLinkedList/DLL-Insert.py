class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        # if in first half
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else: # if in second half, we start from tail to move backwards - more optimal way
            temp = self.tail
            for _ in range (self.length - 1, index, -1): #(start, list, decrement by 1)
                temp = temp.prev

        return temp
            
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        # get nodes before and after index where new node will be
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        # redirect pointers after insertion of new node
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()
my_doubly_linked_list.insert(1,2)
print("----------------")
my_doubly_linked_list.print_list()
