class Tree():
    def __init__(self, id):
        self.left = None
        self.right = None
        self.value = None
        self.parent_id = id

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setLeft(self, node):
        if self.left == None:
            self.left = node

    def setRight(self, node):
        if self.right == None:
            self.right = node

    def getValue(self):
        return self.value
    
    def setValue(self, input_value):
        self.value = input_value


