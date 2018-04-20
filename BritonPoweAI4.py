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

    #print("Number of Positive Tuples:", num_positive)
    #print("Number of Negative Tuples:", num_negative)
    #print("Number of Samples", parent_length)

    if prob_pos != 0 and prob_neg != 0:
        entropy = ((-1*prob_pos)*math.log2(prob_pos))+((-1*prob_neg)*math.log2(prob_neg))

    #print("Entropy:", entropy)
    return entropy


def calculate_IG(samples, attribute):
    
    #print("Current Attribute:", attribute)
    parent_entropy = calculate_entropy(samples, len(samples))
    #print("Parent Entropy:",parent_entropy)
    contains, excludes = has_attribute_split(samples, attribute)
    #print("Contains Entropy:")
    contains_entropy = (float(len(contains)/len(samples)))*calculate_entropy(contains, len(contains))
    #print("Excludes Entropy:")
    excludes_entropy = (float(len(excludes)/len(samples)))*calculate_entropy(excludes, len(excludes))
    #print("Entropy of Contains",contains_entropy)
    #print("Entropy of Excludes",excludes_entropy)
    value_entropy = contains_entropy+excludes_entropy
    info_gain = parent_entropy - value_entropy
    #print("Info Gain:", info_gain)

    return info_gain


def determine_split(samples, num_attributes):
    best_split = 0
    remaining_attributes = []
    highest_gain = -1.0

    sample = samples[0]
    for attribute in range(num_attributes):
        remaining_attributes.append(sample[attribute][0])

    #print(remaining_attributes)

    for attribute in remaining_attributes:
        #print(attribute)
        #for each in samples:
            #print(each)
        current_gain = calculate_IG(samples, attribute)
        #print(current_gain)
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
    if len(samples) == 0:
        print("Class: 0")
        return 0
    if num_attributes == 0:
        if calculate_entropy(samples, len(samples)) == 1:
            print("Class: 1")
            return 0
    if calculate_entropy(samples, len(samples)) == 0.0:
        print("Class:", samples[0][-1][1])
        return samples[0][-1][1]
    
    print("Number of Attributes Left:", num_attributes)
    split = determine_split(samples, num_attributes)

    print("Splitting on", split)

    has, has_not = has_attribute_split(samples, split)
    
    print('\n\nHas List:\n')
    for each in has:
        print(each)
    print('Does not have List:\n')
    for each in has_not:
        print(each)

    
    has = remove_attribute(has, split)
    has_not = remove_attribute(has_not, split)

    
    print("Going left(has)Left Child of",split)
    li1 = copy.deepcopy(has)
    determine_tree(li1, (num_attributes-1))
    print("Going right(doesn't have)Right Child of", split)
    li2 = copy.deepcopy(has_not)
    determine_tree(li2, (num_attributes-1))
    
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

for each in sample_list:
    print(each)

print("\n\n")

determine_tree(sample_list, num_attributes)




