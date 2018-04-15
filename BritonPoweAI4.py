import math

def has_attribute_split(samples, attribute):
    has = []
    has_not = []

    for each in samples:
        if each[attribute] == 1:
            has.append(each)
        else:
            has_not.append(each)

    return has, has_not



def calculate_entropy(samples, parent_length):
    num_samples = len(samples)
    num_positive = 0
    num_negative = 0

    for sample in samples:
        if sample[-1] == 1:
            num_positive += 1
        else:
            num_negative += 1

    prob_pos = float(num_positive/num_samples)
    prob_neg = float(num_negative/num_samples)
    print(prob_pos, prob_neg)
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
    print(parent_entropy)

    contains, excludes = has_attribute_split(testList, attribute)
    print(contains)
    print(excludes)
    contains_entropy = calculate_entropy(contains, len(testList))
    excludes_entropy = calculate_entropy(excludes, len(testList))
    print(contains_entropy,excludes_entropy)
    value_entropy = contains_entropy+excludes_entropy
    print(value_entropy)

    info_gain = parent_entropy - value_entropy

    print(info_gain)



testList = [[1,0,1,1],
            [0,0,1,1],
            [1,1,1,0],
            [1,1,0,0],
            [0,1,1,1],
            [0,0,0,0],]

calculate_IG(testList, 0)
calculate_IG(testList, 1)
calculate_IG(testList, 2)