class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next_node = next

    def get_next (self):
        return self.next_node
    
    def set_next (self, next):
        self.next_node = next

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

class LinkedList (object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size
    
    def add (self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size +=1

    def remove (self, data):
        this_node = self.root # the current node we're looking at
        prev_node = None # starts at rot
        while this_node:
            if this_node.get_data() == data:
                prev_node.set_next(this_node.get_next())
            else:
                self.root = this_node
                self.size -= 1
                return True

