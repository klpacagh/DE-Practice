from calendar import weekday
# kv pairs, one way hash (cannot get the output to produce the input)
# deterministic - produces same output if using same hash
# collisions - one way is called separate chaining, putting at same spot - use lists or linked list
# another is moving down the chain until there's an empty spot - called linear probing (open addressing)
# good idea to use prime numbers as it reduces number of collisions

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord gets ASCII number for each letter
            # we'll use 23 since its prime
            # using the modulo allows us to get an address between 0-6 or length of the hashtable
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key) # computes the address

        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key) # computes the address
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys

# this is O(2n) or O(n) for comparing lists
# using a nested for loop is O(n^2) so the dictionary method is much faster
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False

my_hash_table = HashTable()
my_hash_table.set_item('bolts',1400)
my_hash_table.set_item('washers',50)
my_hash_table.set_item('lumber',70)
my_hash_table.print_table()
print('get item bolts')
print(my_hash_table.get_item('bolts'))
print('get item lumber')
print(my_hash_table.get_item('lumber'))
print("all keys")
print(my_hash_table.keys())

list1=[1,3,5]
list2=[2,4,6]
print("is the above list share similar items?")
print(item_in_common(list1,list2))