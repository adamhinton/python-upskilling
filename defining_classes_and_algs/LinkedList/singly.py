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

