from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.__length = 0

    def isEmpty(self):
        if not (self.front and self.rear):
            return True
        return False

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
            self.rear = new_node
            self.__length = 1
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.__length += 1

    def dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        data = self.front.get_data()
        self.front = self.front.next
        self.__length -= 1
        return data

    def peek(self):
        if not self.front:
            print("Queue is empty")
            return None
        return self.front.get_data()
