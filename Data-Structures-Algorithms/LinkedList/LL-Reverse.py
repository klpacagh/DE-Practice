from sqlalchemy import true


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0: # if we start with 0
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0: # after decrementing and we get 0
            self.head = None
            self.tail = None
        return temp.value # return nodes value we just removed

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0: # applies if we started with 1 item
            self.tail = None

        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # need to iterate through till we get to the specific node
        temp = self.get(index) # using get method

        if temp is not None:
            temp.value = value
            return True
        
        return False
        
    def insert(self, index, value):
        if index < 0 or index >= self.length: # out of range
            return False
        if index == 0: # if adding to first index of 0
            return self.prepend(value)
        if index == self.length: # adding to the end
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1) # want the node before where we want to insert

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length: # out of range
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # need var on right of temp, and var on left of temp (None)
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print("------------------")
my_linked_list.reverse() #rem at index of 1
my_linked_list.print_list()

