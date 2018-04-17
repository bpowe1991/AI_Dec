import math

def has_attribute_split(samples, attribute):
    has = []
    has_not = []

    for each in samples:
        if each[attribute][1] == 1:
            has.append(each)
        else:
            has_not.append(each)

    return has, has_not


def calculate_entropy(samples, parent_length):
    num_samples = len(samples)
    num_positive = 0
    num_negative = 0


    for sample in samples:
        if sample[len(sample)-1][1] == 1:
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

#    print(tested_attribute)


    for attribute in range(num_attributes):
#        if tested_attribute.__contains__(attribute) == False:

            gains_list.append(calculate_IG(samples, attribute))

    print(gains_list)
    best_split = gains_list.index(max(gains_list))

    return samples[0][best_split][0]


def format_input(samples):
    formated_list = []
    for each in samples:
        sample =[]
        count = 0
        for attribute in each:
            sample.append((count,attribute))
            count += 1
        formated_list.append(sample)

    return formated_list

def remove_attribute(samples, attribute):
    for each in samples:
        del each[attribute]

    return samples

def determine_tree(samples, num_attributes):

    print("Current List:")
    for each in samples:
        print(each)

    print("\n\n")

    
    if calculate_entropy(samples, len(samples)) == 0:
        print("Leaf Node")
        return
    
    split = determine_split(samples, num_attributes)
    
    print("Current Split:")
    print(split, "\n\n")

    contains, not_contains = has_attribute_split(samples, split)
    
    print("Has Attribute List:")
    for each in contains:
        print(each)

    print("\n\n")

    print("Doesn't Has Attribute List:")
    for each in not_contains:
        print(each)
    
    print("\n\n")
    
    contains = remove_attribute(contains, split)
    not_contains = remove_attribute(not_contains, split)
    
    print("Has Attribute List:")
    for each in contains:
        print(each)

    print("\n\n")

    
    for each in not_contains:
        print(each)

    print("Going left")
    determine_tree(contains, num_attributes-1)
    print("Going right")
    determine_tree(not_contains, num_attributes-1)

    

tested_attribute = []

#***** vars *****/

testList = [[1,0,1,1],
            [0,0,1,1],
            [1,1,1,0],
            [1,1,1,0],
            [0,1,1,1],
            [0,0,0,0],
            [1,0,0,0],
            [1,1,0,0],
            [1,0,0,1],
            [1,1,0,1]]

tested = []
testList = format_input(testList)
determine_tree(testList, 3)





# main

#traverse(testList);
#printReport()



# def traverse(tree){
#     if (first){
#         do extra stuff    
#     }
#     if (entropy == 0) return

#     testList = format_input(testList)
#     tested_attribute = []

#     split = determine_split(testList, 3)
#     tested_attribute.append(split)
#     print("Attribute", split, "has the best information gain")

#     new_list1, new_list2 = has_attribute_split(testList, split)

#     print(new_list1, "\n"+str(new_list2))

#     split = determine_split(new_list1, 3)
#     tested_attribute.append(split)
#     print("Attribute", split, "has the best information gain")

#     traverse(modifiedTreeSubset)
# }