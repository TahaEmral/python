import unittest

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def setNext(self, next_node = None):
        self.next = next_node


def has_cycle(head):
    if head == None:
        return False
    
    slow = fast = head
    
    while(slow or fast or fast.next):
        
        if fast.next == None:
            return False
        
        if slow == fast.next or slow == fast.next.next:
            return True
        
        slow = slow.next
        fast = fast.next.next

    return False

class TestStringMethods(unittest.TestCase):

    def test_loop_empty(self):
        self.assertEqual(has_cycle(None), False)

    def test_loop(self):
        self.assertEqual(has_cycle(n5), True)

    def test_no_loop(self):
        self.assertEqual(has_cycle(m5), False)


n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5, n4)

n2.setNext(n4) # Loop

m1 = Node(1, None)
m2 = Node(2, m1)
m3 = Node(3, m2)
m4 = Node(4, m3)
m5 = Node(5, m4)


unittest.main()