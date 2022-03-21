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

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

# (2) items return 2 node
print(my_linked_list.pop())
# (1) item returns 1 node
print(my_linked_list.pop())
# (0) items returns None
print(my_linked_list.pop())
                                  