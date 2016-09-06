class Node(object):
    """Linked list node class"""

    def __init__(self, data=None, next=None):
        self.val = data
        self.next = None

    def __repr__(self):
        return "%s" %str(self.val)

class LinkedList(object):
    """Linked list implementation"""

    def __init__(self, head=None):

        self.head = head

    def insert(self, data):
        """Inserts node at beginning of ll"""

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):

        current = self.head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev

    def delete(self, data):
        """Delete node with specified data from list"""

        current = self.head
        prev = None

        while current:
            if current.val == data:
                if not prev: # If at start of list
                    self.head = current.next
                else:
                    prev.next = current.next
                current.next = None
                return self

            else:
                prev = current
                current = current.next

        print "Could not find node with specified data"

    def to_string(self):

        ll = ''

        current = self.head

        while current:
            if ll:
                ll = ll + '-->' + str(current.val)
            else:
                ll = ll + str(current.val)
            current = current.next

        return ll

    def __repr__(self):

        data_string = self.to_string()
        return "%s" % data_string
