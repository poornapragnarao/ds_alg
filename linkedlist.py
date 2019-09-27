class Element(object):
    def __init__(self, val=None):
        self.value = val
        self.next = None


class LinkedList(object):
    def __init__(self, elem=None):
        self.head = elem

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_element_at(self, position):
        ret_elem = None
        current = self.head
        while position > 1:
            position = position - 1
            current = current.next
        ret_elem = current
        return ret_elem

    def insert(self, element, position):
        previous = self.head
        while position > 2:
            position = position - 1
            previous = previous.next
        push_elem = previous.next
        previous.next = element
        element.next = push_elem

    def delete(self, value):
        current = self.head
        previous = None
        found = True
        while current.value != value:
            previous = current
            if not current.next:
                found = False
                break
            current = current.next
        if not found:
            return
        if not previous:
            # Delete the head
            self.head = self.head.next
        else:
            # Not first element
            previous.next = current.next

    def get_all_as_list(self):
        ret_list = []
        current = self.head
        if not current:
            return ret_list

        while current:
            ret_list.append(current.value)
            current = current.next
        return ret_list



e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList()

ll.append(e1)
ll.append(e2)
ll.append(e3)

print(ll.get_all_as_list())

ll.insert(e4, 3)

print(ll.get_all_as_list())

ll.delete(3)

print(ll.get_all_as_list())


