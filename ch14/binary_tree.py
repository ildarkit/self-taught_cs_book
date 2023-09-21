class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        btree = BinaryTree(value)
        if self.left_child is None:
            self.left_child = btree
        else:
            btree.left_child = self.left_child
            self.left_child = btree

    def insert_right(self, value):
        btree = BinaryTree(value)
        if self.right_child is None:
            self.right_child = btree
        else:
            btree.right_child = self.right_child
            self.right_child = btree

    def invert_bfs(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []

    def invert_postorder(self):
        self._invert_postorder(self)

    def _invert_postorder(self, tree):
        if tree: 
            self._invert_postorder(tree.left_child)
            self._invert_postorder(tree.right_child)
            tree.left_child, tree.right_child = (
                tree.right_child,
                tree.left_child
            )

    def inorder(self):
        self._inorder(self)

    def _inorder(self, tree):
        if tree:
            self._inorder(tree.left_child)
            print(tree.key)
            self._inorder(tree.right_child)

    def has_leaf_nodes(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if (node.left_child is None and
                        node.right_child is None):
                    return True 
                if node.left_child is None:
                    next.append(node.right_child)
                else:
                    next.append(node.left_child)
            current = next
            next = []
        return False


if __name__ == '__main__':
    binary_tree = BinaryTree(1)
    binary_tree.insert_left(2)
    binary_tree.insert_right(3)
    binary_tree.insert_left(4)
    binary_tree.left_child.insert_right(6)
    binary_tree.insert_right(5)
    assert binary_tree.has_leaf_nodes()
    binary_tree.invert_postorder()
    binary_tree.inorder()

