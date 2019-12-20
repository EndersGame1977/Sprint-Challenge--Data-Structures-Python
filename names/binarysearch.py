class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self.value

        # if value less than current that's not the end

        if value < current_node:

            if self.left is None:
                self.left = BinarySearchTree(value)
                return  # insert to the end
            else:
                left_node = self.left
                left_node.insert(value)

        if value > current_node:

            # then that's the end, insert in the beggining
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                right_node = self.right
                right_node.insert(value)

    def contains(self, target):  # same idea from above but for contain
        current_node = self.value

        if current_node == target:
            return True

        if target < current_node:

            if self.left is None:
                return False
            else:
                left_node = self.left
                return left_node.contains(target)

        if target > current_node:
            if self.right is None:
                return False
            else:
                right_node = self.right
                return right_node.contains(target)
