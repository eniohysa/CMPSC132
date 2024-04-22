from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if not self.top:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.isEmpty():
            print('Empty stack')
            return None
        data = self.top.get_data()
        self.top = self.top.next
        return data

    def peek(self):
        if self.isEmpty():
            print('Empty stack')
            return None
        return self.top.get_data()

    def display(self):
        if self.isEmpty():
            print('Empty')
        else:
            current = self.top
            while current:
                print(current.get_data(), end=' -> ')
                current = current.next
            print('End')


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.display()
