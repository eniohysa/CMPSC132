from TreeNode import TreeNode


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while current:
                if new_node.get_data() <= current.get_data():
                    if not current.left:
                        current.left = new_node
                        return
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = new_node
                        return
                    else:
                        current = current.right

    def search(self, data):
        if not self.root:
            print('Empty')
            return
        current = self.root
        while current:
            if current.get_data() == data:
                print('Found')
                return True
            elif current.get_data() > data:
                current = current.left
            else:
                current = current.right
        return None

    def remove(self, key):
        par = None
        cur = self.root
        while cur:
            if key == cur.get_data():
                if not cur.left and not cur.right:
                    if not par:
                        print(f'fThe last node {cur.get_data()} is removed')
                        self.root = None
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right = None
                    print(f'The last node {cur.get_data()} is removed')
                elif not cur.left:
                    if par.left == cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right
                elif not cur.right:
                    if par.right == cur:
                        par.right = cur.right
                    else:
                        par.left = cur.left
                else:
                    successor = cur.right
                    while successor.left:
                        successor = successor.left
                    self.remove(successor.get_data())
                return
            elif key < cur.get_data():
                par = cur
                cur = cur.left
            else:
                par = cur
                cur = cur.right
        print(f'Node with key {key} not found')

    def display(self):
        self.__printInOrder(self.root)

    def __printInOrder(self, node):
        if node is None:
            return None
        self.__printInOrder(node.left)
        print(node)
        self.__printInOrder(node.right)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)
    tree.insert(10)
    tree.display()
    tree.remove(6)
    tree.display()

