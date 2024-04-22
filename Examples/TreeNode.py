class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.__data = data

    def get_data(self):
        return self.__data

    def __str__(self):
        return f'{self.get_data()}'
    