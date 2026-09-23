import math

def entropy(data):
    total = len(data)
    answer = 0
    
    for value in set(data):
        count = data.count(value)
        probability = count / total 
        answer -= probability * math.log2(probability)  
    return answer
    
