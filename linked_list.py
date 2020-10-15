class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1
        return True

    def delete_node(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.get_data() == value:
                if prev:
                    prev.set_next(curr.get_next())
                else:
                    self.head = curr.get_next()
                return True
            prev = curr
            curr = curr.get_next()
        return False

    def find_node(self, value):
        curr = self.head
        while curr:
            if curr.get_data() == value:
                return True
            else:
                curr = curr.get_next()
        return False

    def print(self):
        node = self.head
        while node:
            print(node.get_data())
            node = node.get_next()


mylist = LinkedList()
mylist.add_node(5)
mylist.add_node(15)
mylist.add_node(25)
print(mylist.find_node(1))
mylist.print()

