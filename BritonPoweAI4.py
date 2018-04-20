import math
import copy
from Tree import Tree

def has_attribute_split(samples, attribute):
    has = []
    has_not = []

    for sample in samples:
        for item in sample: 
            if item[0] == attribute:
                if item[1] == 1:
                    has.append(sample)
                else:
                    has_not.append(sample)

    return has, has_not


def calculate_entropy(samples, parent_length):
    
    if parent_length == 0:
        return 0
    
    num_samples = parent_length    
    num_positive = 0
    num_negative = 0


    for sample in samples:
        if sample[-1][1] == 1:
            num_positive += 1
        else:
            num_negative += 1

    prob_pos = float(num_positive/num_samples)
    prob_neg = float(num_negative/num_samples)
    entropy = 0

    if prob_pos != 0 and prob_neg != 0:
        entropy = ((-1*prob_pos)*math.log2(prob_pos))+((-1*prob_neg)*math.log2(prob_neg))

    return entropy


def calculate_IG(samples, attribute):
    
    parent_entropy = calculate_entropy(samples, len(samples))

    contains, excludes = has_attribute_split(samples, attribute)

    contains_entropy = (float(len(contains)/len(samples)))*calculate_entropy(contains, len(contains))

    excludes_entropy = (float(len(excludes)/len(samples)))*calculate_entropy(excludes, len(excludes))

    value_entropy = contains_entropy+excludes_entropy
    info_gain = parent_entropy - value_entropy


    return info_gain


def determine_split(samples, num_attributes):
    best_split = 0
    remaining_attributes = []
    highest_gain = -1.0

    sample = samples[0]
    for attribute in range(num_attributes):
        remaining_attributes.append(sample[attribute][0])

    for attribute in remaining_attributes:

        current_gain = calculate_IG(samples, attribute)

        if current_gain > highest_gain:
            highest_gain = current_gain
            best_split = attribute

    return best_split


def format_input(samples):
    formated_list = []
    for each in samples:
        sample =[]
        count = 1
        for attribute in each:
            sample.append((count,int(attribute)))
            count += 1
        formated_list.append(sample)

    return formated_list

def remove_attribute(samples, attribute):
    
    index = 0
    for sample in samples:
        for each in sample:
            if each[0] == attribute:
                index = sample.index(each)


    for sample in samples:
        del sample[index]
        

    return samples

def determine_tree(samples, num_attributes):
    global pre_order, in_order

    if len(samples) == 0:
        pre_order.append("N")
        in_order.append("N")
        return 
    if num_attributes == 0:
        if calculate_entropy(samples, len(samples)) == 1:

            pre_order.append("Y")
            in_order.append("Y")
            return 
    if calculate_entropy(samples, len(samples)) == 0.0:
        if samples[0][-1][1] == 1:
            pre_order.append("Y")
            in_order.append("Y")
        else:
            pre_order.append("N")
            in_order.append("N")
        return 
    

    split = determine_split(samples, num_attributes)

    has, has_not = has_attribute_split(samples, split)
    
    has = remove_attribute(has, split)
    has_not = remove_attribute(has_not, split)

    pre_order.append(split)
    
    li1 = copy.deepcopy(has)
    determine_tree(li1, (num_attributes-1))
    
    in_order.append(split)

    li2 = copy.deepcopy(has_not)
    determine_tree(li2, (num_attributes-1))


def construct_tree(in_order, pre_order, start_index, end_index):

    if start_index > end_index:
        return None

    node = Tree(pre_order[construct_tree.starter])
    construct_tree.starter += 1

    if start_index == end_index:
        return node

    index = search_value(in_order, start_index, end_index, node.getValue())

    node.setLeft(construct_tree(in_order, pre_order, start_index, index-1))
    node.setRight(construct_tree(in_order, pre_order, index+1, end_index))
    
    return node



def search_value(in_order, start_value, end_value, value):
    for index in range(start_value, end_value+1):
        if in_order[index] == value:
            return index

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


#Opening input file called input.txt
input = open('input.txt', 'r')


construct_tree.starter = 0

#Getting parameters of input
sample_list = []
parameters = input.readline()
parameters = parameters.split()

#Setting numbeer of attributes and number of samples
num_attributes = int(parameters[0])
num_samples = int(parameters[1])

#Creating input sample list
for line in input:
    line = line.rstrip('\n')
    sample_list.append(line.split())

print("Input Sample List:")
for each in sample_list:
    print(each)
print("\n")

#Formatting list
sample_list = format_input(sample_list)



in_order = []
pre_order = []

determine_tree(sample_list, num_attributes)

head = construct_tree(in_order, pre_order, 0, len(in_order)-1)

printTree(head)

def determine_class(sample):
    global head
    pointer = head
    while pointer.getValue() != "Y" and pointer.getValue() != "N":
        if sample[pointer.getValue()-1][1] == 1:
            pointer = pointer.getLeft()
        else:
            pointer = pointer.getRight()
    
    if pointer.getValue() == "Y":
        print("Class is 1 - (True)")
    else:
        print("Class is 0 - (False)")

determine_class([(1,1),(2,1),(3,0),(4,0),(5,1),(6,1),(7,1),(8,1),(9,0),(10,1)])



