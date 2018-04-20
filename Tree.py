class Tree():
    def __init__(self, id):
        self.__left = None
        self.__right = None
        self.__value = id
        self.__parent_id = None

    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def setLeft(self, node):
        if self.__left == None:
            self.__left = node

    def setRight(self, node):
        if self.__right == None:
            self.__right = node

    def getValue(self):
        return self.__value
    
    def setValue(self, input_value):
        self.__value = input_value
    
    def setParent(self, parent):
        self.__parent_id = parent


