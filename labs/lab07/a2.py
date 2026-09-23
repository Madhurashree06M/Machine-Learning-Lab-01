def gini_index(data):
    total = len(data) 
    probabilities = []  
    for value in set(data):
        count = data.count(value)
        probability = count / total
        probabilities.append(probability)  
    gini = 1 
    for p in probabilities:
        gini -= p ** 2
    return gini