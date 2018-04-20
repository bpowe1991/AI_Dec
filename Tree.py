""""
Programmer: Briton A. Powe          Program Homework Assignment #4
Date: 4/19/18                       Class: Introduction to A.I.
Version: 1.9.1
File: Tree.py
------------------------------------------------------------------------
Program Description:
File for Tree class. Tree class is used to build decision tree
***This program uses Python 3.6.4***
"""

#Tree class used to construct decision tree
class Tree():
    
    #Constructor
    def __init__(self, id):
        self.__left = None
        self.__right = None
        self.__value = id
        self.__parent_id = None

    #Function to get left child
    def getLeft(self):
        return self.__left
    
    #Function to get right child
    def getRight(self):
        return self.__right
    
    #Function to set left child
    def setLeft(self, node):
        if self.__left == None:
            self.__left = node

    #Function to set right child
    def setRight(self, node):
        if self.__right == None:
            self.__right = node

    #Function to get node value. Leaves have Y or N.
    #Root and internal nodes have attribute number
    def getValue(self):
        return self.__value
    
    #Function to set value
    def setValue(self, input_value):
        self.__value = input_value
    
    #Function to set parent
    def setParent(self, parent):
        self.__parent_id = parent
    
    #Function to get parent
    def getParent(self):
        return self.__parent_id


