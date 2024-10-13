from bin import Bin  # Add this import statement

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return AVLNode(value)

        if isinstance(value, Bin):
            if value.bin_id < node.value.bin_id:
                node.left = self._insert(node.left, value)
            else:
                node.right = self._insert(node.right, value)
        else:  # Assuming value is an Object
            if value.object_id < node.value.object_id:
                node.left = self._insert(node.left, value)
            else:
                node.right = self._insert(node.right, value)

        self.update_height(node)
        balance = self.get_balance(node)

        if isinstance(value, Bin):
            if balance > 1 and value.bin_id < node.left.value.bin_id:
                return self.rotate_right(node)
            if balance < -1 and value.bin_id > node.right.value.bin_id:
                return self.rotate_left(node)
            if balance > 1 and value.bin_id > node.left.value.bin_id:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            if balance < -1 and value.bin_id < node.right.value.bin_id:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        else:  # Object balance cases
            if balance > 1 and value.object_id < node.left.value.object_id:
                return self.rotate_right(node)
            if balance < -1 and value.object_id > node.right.value.object_id:
                return self.rotate_left(node)
            if balance > 1 and value.object_id > node.left.value.object_id:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            if balance < -1 and value.object_id < node.right.value.object_id:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return node

        if isinstance(value, Bin):
            if value.bin_id < node.value.bin_id:
                node.left = self._delete(node.left, value)
            elif value.bin_id > node.value.bin_id:
                node.right = self._delete(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.get_min_value_node(node.right)
                node.value = temp.value
                node.right = self._delete(node.right, temp.value)
        else:  # Object deletion
            if value.object_id < node.value.object_id:
                node.left = self._delete(node.left, value)
            elif value.object_id > node.value.object_id:
                node.right = self._delete(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.get_min_value_node(node.right)
                node.value = temp.value
                node.right = self._delete(node.right, temp.value)

        self.update_height(node)
        balance = self.get_balance(node)

        if isinstance(value, Bin):
            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        else:  # Object balancing
            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
