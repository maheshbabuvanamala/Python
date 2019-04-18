class Node:
    """ Node in Linked List """
    def __init__(self,value):
        self.data=value
        self.next=None
    def set_data(self,data):
        self.data=data
    def get_data(self):
        return self.data
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next
    def hasNext(self):
        return self.next!=None
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    """ Traversing Element """
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.get_data())
            current=current.get_next()
a=LinkedList()
a.insert(10)
a.insert(11)
a.insert(12)
a.traverse()
