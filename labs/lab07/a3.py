import math

def entropy(data):
    total = len(data)
    answer = 0
    
    for value in set(data):
        count = data.count(value)
        probability = count / total
        answer -= probability * math.log2(probability)
    return answer

def weighted(data, feature):
    total = len(data)
    weighted_entropy = 0
    for i in set(feature):
        subset = []
        for j in range(len(feature)):
            if feature[j] == i:
                subset.append(data[j])

        probability = len(subset) / total
        weighted_entropy += probability * entropy(subset)
    return weighted_entropy

def info_gain(data, feature):
    return entropy(data) - weighted(data, feature)

def root(data, features):
    gains = {}
    for name, feature in features.items():
        gains[name] = info_gain(data, feature)
    root = max(gains, key=gains.get)
    return root, gains