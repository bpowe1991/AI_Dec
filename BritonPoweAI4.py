import math
import copy

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
    
    if len(samples) == 0:
        return 0
    num_samples = len(samples)    
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

    if prob_pos == 0 and prob_neg != 0:
        entropy = (-1*prob_neg)*math.log2(prob_neg)
    elif prob_neg == 0 and prob_pos != 0:
        entropy = (-1*prob_pos)*math.log2(prob_pos)
    elif prob_pos != 0 and prob_neg != 0:
        entropy = ((-1*prob_pos)*math.log2(prob_pos))+((-1*prob_neg)*math.log2(prob_neg))
    

    entropy *= float(num_samples/parent_length)

    return entropy


def calculate_IG(samples, attribute):
    
    parent_entropy = calculate_entropy(samples, len(samples))
    contains, excludes = has_attribute_split(samples, attribute)
    contains_entropy = calculate_entropy(contains, len(samples))
    excludes_entropy = calculate_entropy(excludes, len(samples))
    value_entropy = contains_entropy+excludes_entropy
    info_gain = parent_entropy - value_entropy

    return info_gain


def determine_split(samples, num_attributes):
    best_split = 0
    gains_list = []
    remaining_attributes = []

    sample = samples[0]
    for attribute in range(num_attributes):
        remaining_attributes.append(sample[attribute][0])

    print(remaining_attributes)


#    print(tested_attribute)


    for attribute in remaining_attributes:
        print(attribute)
        for each in samples:
            print(each)
        gains_list.append(calculate_IG(samples, attribute))

    print(gains_list)
    best_split = gains_list.index(max(gains_list))

    return samples[0][best_split][0]


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
    
    for each in samples:
        print(each)
    current_entropy = calculate_entropy(samples, len(samples))
    if current_entropy == 0 or num_attributes == 0:
        print("Leaf node(class):")
        print(samples[0][-1][1])
        return

    split = determine_split(samples, num_attributes)

    print(split)

    has, has_not = has_attribute_split(sample_list, split)

    # print('\n\n')
    # print(has)
    # print('\n')
    # print(has_not)

    has = remove_attribute(has, split)
    has_not = remove_attribute(has_not, split)

    print('\n\n')
    print(has)
    print('\n')
    print(has_not)
    print("Going left(has)")
    li1 = copy.deepcopy(has)
    determine_tree(li1, num_attributes-1)
    print("Going right(doesn't have)")
    li2 = copy.deepcopy(has_not)
    determine_tree(li2, num_attributes-1)
    
#Opening input file called input.txt
input = open('input.txt', 'r')

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

#Formatting list
sample_list = format_input(sample_list)
        
determine_tree(copy.deepcopy(sample_list), num_attributes)

# print(split)

# has, has_not = has_attribute_split(has, split)
# has = remove_attribute(has, split)
# has_not = remove_attribute(has_not, split)

# print('\n\n')
# print(has)
# print('\n')
# print(has_not)
# print("Going left(has)")

# current_entropy = calculate_entropy(has, len(has))

# print(current_entropy)


#determine_tree(sample_list, num_attributes)






















# main

#traverse(testList);
#printReport()



# def traverse(tree){
#     if (first){
#         do extra stuff    
#     }
#     if (entropy == 0) return
#     split = determine_split(testList, 3)
#     print("Attribute", split, "has the best information gain")

#     new_list1, new_list2 = has_attribute_split(testList, split)

#     print(new_list1, "\n"+str(new_list2))

#     split = determine_split(new_list1, 3)
#     tested_attribute.append(split)
#     print("Attribute", split, "has the best information gain")

#     traverse(modifiedTreeSubset)
# }