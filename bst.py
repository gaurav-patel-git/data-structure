class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        cur_node = self.root
        if cur_node is None:
            return None
        while cur_node.value != None:
            if key < cur_node.value:
                prv_node = cur_node
                cur_node = cur_node.left

            elif key > cur_node.value:
                prv_node = cur_node
                cur_node = cur_node.right
            else:
                break
        return prv_node

    def inset(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            cur_node = self.root
            new_node = Node(value)
            while cur_node != None:
                if value < cur_node.value:
                    if cur_node.left is None:
                        cur_node.left = new_node
                    cur_node = cur_node.left
                elif value > cur_node.value:
                    if cur_node.right is None:
                        cur_node.right = new_node
                    cur_node = cur_node.right
                else:
                    cur_node = None

    def post_order(self):
        print(self._post_order(self.root, ""))

    def _post_order(self, cur_node, traversal):
        if cur_node:
            traversal = self._post_order(cur_node.left, traversal)
            traversal = self._post_order(cur_node.right, traversal)
            traversal += str(cur_node.value) + "-"
        return traversal

tree = BST()
tree.inset(5)
tree.inset(16)
tree.inset(15)
tree.inset(2)
tree.inset(3)
tree.inset(1)
tree.inset(55)
tree.post_order()
