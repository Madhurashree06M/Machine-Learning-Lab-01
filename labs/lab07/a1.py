import numpy as num

def entropy(data):
    values, counts = num.unique(data, return_counts=True)
    
    probabilities = counts / len(data)
    
    entropy_value = 0
    for p in probabilities:
        entropy_value -= p * num.log2(p)
    
    return entropy_value
