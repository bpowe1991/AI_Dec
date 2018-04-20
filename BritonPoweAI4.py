""""
Programmer: Briton A. Powe          Program Homework Assignment #4
Date: 4/19/18                       Class: Introduction to A.I.
Version: 1.9.1
File: BritonPoweAI4.py
------------------------------------------------------------------------
Program Description:
Program to construct a decision tree using user defined input file.
The user then can classify a sample based on the constructed decision tree.
***This program uses Python 3.6.4***

References:
For building tree based on in-order and pre-order:
https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

For constructing binary tree in python:
http://pythonschool.net/data-structures-algorithms/binary-tree/

For entropy and information gain calculation:
http://www.saedsayad.com/decision_tree.htm

"""

import math
import copy

#Importing the Tree class
from Tree import Tree

#Function to split list based on attribute
def has_attribute_split(samples, attribute):
    has = []
    has_not = []

    #Loop to divide list into sublist
    for sample in samples:
        for item in sample: 
            if item[0] == attribute:
                if item[1] == 1:
                    has.append(sample)
                else:
                    has_not.append(sample)

    #Return list divide by the presence of an attribute
    return has, has_not

#Function to calculate entropy
def calculate_entropy(samples, parent_length):
    
    #If list is empty return 0
    if parent_length == 0:
        return 0
    
    num_samples = parent_length    
    num_positive = 0
    num_negative = 0

    #Reading values for each sample
    for sample in samples:
        if sample[-1][1] == 1:
            num_positive += 1
        else:
            num_negative += 1

    #Setting fractions for calculations
    prob_pos = float(num_positive/num_samples)
    prob_neg = float(num_negative/num_samples)
    entropy = 0

    #If the positive and negative values are not 0
    if prob_pos != 0 and prob_neg != 0:
        entropy = ((-1*prob_pos)*math.log2(prob_pos))+((-1*prob_neg)*math.log2(prob_neg))

    return entropy

#Function to calculate info gain
def calculate_IG(samples, attribute):
    
    parent_entropy = calculate_entropy(samples, len(samples))

    #Split list for entropy calculations
    contains, excludes = has_attribute_split(samples, attribute)

    #Entropy for list with attribute
    contains_entropy = (float(len(contains)/len(samples)))*calculate_entropy(contains, len(contains))

    #Entropy for list without attribute
    excludes_entropy = (float(len(excludes)/len(samples)))*calculate_entropy(excludes, len(excludes))

    value_entropy = contains_entropy+excludes_entropy
    
    #Calculating information gain
    info_gain = parent_entropy - value_entropy


    return info_gain

#Function to determine best attribute to split on
def determine_split(samples, num_attributes):
    best_split = 0
    
    #List to track remaining attributes in samples
    remaining_attributes = []
    highest_gain = -1.0

    #Retrieving remaing attributes
    sample = samples[0]
    for attribute in range(num_attributes):
        remaining_attributes.append(sample[attribute][0])

    #Testing each remaining attribute for best based on info gain
    for attribute in remaining_attributes:

        current_gain = calculate_IG(samples, attribute)

        #Keep the highest gain with cooresponding attribute
        if current_gain > highest_gain:
            highest_gain = current_gain
            best_split = attribute

    return best_split

#Function to format input from input file
def format_input(samples):
    formated_list = []
    
    #Assigning a number to each attribute to keep track
    for each in samples:
        sample =[]
        count = 1
        for attribute in each:
            sample.append((count,int(attribute)))
            count += 1
        formated_list.append(sample)

    return formated_list

#Function to remove an atrribute from a list
def remove_attribute(samples, attribute):
    index = 0

    #Finding index of attribute
    for sample in samples:
        for each in sample:
            if each[0] == attribute:
                index = sample.index(each)

    #Removing attribute
    for sample in samples:
        del sample[index]
        

    return samples

#Function that recursively determines the tree
#Uses global list to note the in-order and pre-order of tree
def determine_tree(samples, num_attributes):
    global pre_order, in_order

    #Conditions for leaf nodes
    if len(samples) == 0:
        
        #Adding Leaf nodes to repective lists
        pre_order.append("N")
        in_order.append("N")
        return 
    if num_attributes == 0:
        if calculate_entropy(samples, len(samples)) == 1:

            #Adding leaf nodes when final entropy is 50/50
            pre_order.append("Y")
            in_order.append("Y")
            return 
    if calculate_entropy(samples, len(samples)) == 0.0:
        
        #Adding entropy when calculated to 0
        if samples[0][-1][1] == 1:
            pre_order.append("Y")
            in_order.append("Y")
        else:
            pre_order.append("N")
            in_order.append("N")
        return 
    
    #Getting best split
    split = determine_split(samples, num_attributes)

    #Dividing the list
    has, has_not = has_attribute_split(samples, split)
    
    #Removing attribute
    has = remove_attribute(has, split)
    has_not = remove_attribute(has_not, split)

    #Adding node to pre-order
    pre_order.append(split)
    
    #Traversing left subtree
    li1 = copy.deepcopy(has)
    determine_tree(li1, (num_attributes-1))
    
    #Adding node to in-order
    in_order.append(split)

    #traversing right subtree
    li2 = copy.deepcopy(has_not)
    determine_tree(li2, (num_attributes-1))

    del li1, li2

#Function to construct tree using in-order and pre-order
def construct_tree(in_order, pre_order, start_index, end_index):

    #Ensure no index error
    if start_index > end_index:
        return None

    #Constructing node
    node = Tree(pre_order[construct_tree.starter])
    
    #Updating starting index
    construct_tree.starter += 1

    #When list ends returns current node
    if start_index == end_index:
        return node

    #calculating dividing index based on pre-order list
    index = search_value(in_order, start_index, end_index, node.getValue())

    #Creating left subtree
    node.setLeft(construct_tree(in_order, pre_order, start_index, index-1))

    #Creating right subtree
    node.setRight(construct_tree(in_order, pre_order, index+1, end_index))
    
    #return the root node
    return node

#Function to find index in in-order based on pre-order
def search_value(in_order, start_value, end_value, value):
    
    #Looping through list until match is found
    for index in range(start_value, end_value+1):
        if in_order[index] == value:
            return index

#Function to print the structure of the tree
def printTree(tree):
    global head
    
    if tree != None:
        if tree.getValue() == head.getValue():
            print("::Root::")
        if tree.getValue() == "Y" or tree.getValue() == "N":
            print("::Leaf::")
        print("Current Node:", tree.getValue())
        if tree.getLeft() != None:
            print("Left Child:", tree.getLeft().getValue())
        if tree.getRight() != None:
            print("Right Child:", tree.getRight().getValue())
        print("\n")
        printTree(tree.getLeft())
        printTree(tree.getRight())

#Function to determine class based on sample input
def determine_class(sample):
    global head
    pointer = head
    
    #Traversing tree based on attribute values of sample. 1 go left. 0 go right
    while pointer.getValue() != "Y" and pointer.getValue() != "N":
        if sample[pointer.getValue()-1][1] == 1:
            pointer = pointer.getLeft()
        else:
            pointer = pointer.getRight()
    
    #Determine class based on ending leaf node 
    if pointer.getValue() == "Y":
        print("Class is 1 - (True)")
    else:
        print("Class is 0 - (False)")

#Loop for getting filename and reading input file
filename = None

while filename is None:
    try:
        filename = input("Please enter the name of the input file: ")
        
        #Opening input file called input.txt
        input_data = open(filename, 'r')
    except OSError:
        print('\nError accessing file. Enter the correct filename with extension.\n\n')
        filename = None
    
#Preset for start index for construct_tree function
construct_tree.starter = 0

#Getting parameters of input
sample_list = []
parameters = input_data.readline()
parameters = parameters.split()

#Setting numbeer of attributes and number of samples
num_attributes = int(parameters[0])
num_samples = int(parameters[1])

#Creating input sample list and parsing
for line in input_data:
    line = line.rstrip('\n')
    sample_list.append(line.split())

print("Input Sample List:")
for each in sample_list:
    print(each)
print("\n")

#Formatting list for program to read
sample_list = format_input(sample_list)

#Global lists for tree in-order and pre-order
in_order = []
pre_order = []

#Determining tree and building global lists
determine_tree(sample_list, num_attributes)

#Building and tracking tree
head = construct_tree(in_order, pre_order, 0, len(in_order)-1)

#Printing tree structure
print(":::Tree Structure:::")
printTree(head)

#Loop to test samples
choice = "Y"

while choice == "Y":
        choice = input("Would you like to test a sample (Y/N)?:")
        choice = choice.upper()
        if choice != "Y" and choice != "N":
            print("Invalid Input. Please enter either Y or N.")
            choice = "Y"
        elif choice == "Y":
            print("\n")
            test_sample = []
            for x in range(1, num_attributes+1):
                user_input = None

                while user_input is None:
                    try:
                        user_input = input("Please Enter the value for Attribute ("+str(x)+"):")
                        user_input = int(user_input)
                        if user_input != 1 and user_input != 0:
                            print("\nError! Please enter either 1 or 0")
                            user_input = None
                        else:
                            test_sample.append((x, user_input))
                    except ValueError:
                        print("\nError! Please enter either 1 or 0")

            #Determine class based on input
            print("\n")
            determine_class(test_sample)
            print("\n")

print("\nEnd of Program. Goodbye!")

input_data.close()



