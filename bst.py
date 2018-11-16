class NodeBST:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
# Compare the new value with the parent NodeBST
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = NodeBST(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = NodeBST(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Use the add method to add NodeBSTs
'''
root = NodeBST(10)
root.add(3)
root.add(7)
root.add(4)
root.add(20)
root.add(15)

root.PrintTree()
'''