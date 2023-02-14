class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, next_node):
        self.next_node = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            current = current.get_next()
        return None
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            return
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    def print_list(self):
        current = self.head
        while current:
            print(current.get_data(),end=" -> ")
            current = current.get_next()
        print("None")


ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.print_list()
ll.size()
ll.search(2)
