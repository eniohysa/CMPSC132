# this is the linked list class (ADT)
from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, value):
        current = self.head
        while current:
            if current.get_data() == value:
                print('Found')
                return True
            else:
                current = current.next
        print(f"{value} is not in list")
        return False

    def delete(self, data):
        if self.head:
            if self.head.get_data() == data:
                self.head = self.head.next
            else:
                current = self.head
                previous = None
                while current.next:
                    if current.get_data() == data:
                        previous.next = current.next
                        return True
                    previous = current
                    current = current.next

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif self.tail.get_data() <= value:
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next and current.get_data() < value and current.next.get_data():
                current = current.next
            if self.head.get_data() < value:
                pass
            new_node.next = current.next
            current.next = new_node

    def search2(self, item):
        return self.__recursive_search(item, self.head)

    def __recursive_search(self, item, node):
        if node:
            if node.get_data() == item:
                return True
            return self.__recursive_search(item, node.next)
        return False

    def sort(self):
        current = self.head
        while current:
            min_node = current
            next = current.next
            while next:
                if next.get_data() < min_node.get_data():
                    min_node = next
                next = next.next
            self.swap_nodes(current, min_node)
            current = current.next

    def swap_nodes(self, node1, node2):
        tmp = node2.get_data()
        node2.set_data(node1.get_data())
        node1.set_data(tmp)



    def display(self):
        current = self.head
        while current:
            print(current.get_data(), end=" -> ")
            current = current.next
        print('Done')


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(5.5)
    list1.append(2.5)
    list1.append(10.5)
    list1.append(12.0)
    list1.append(6.0)
    list1.append(1.25)
    list1.append(15.0)
    list1.append(7.5)
    list1.display()
    list1.sort()
    list1.display()
