import math
# Distance Calculation: based on selected mode, distance my be calculated using any metrics. 

def euclidean(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * A[i]
    ans = math.sqrt(sum)
    return ans

def minkowski(x, y, p): 
    summation = 0
    for i in range(len(x)):
        summation += (abs(x[i]-y[i]))**p 

    dist = summation ** (1/p)
    return dist

def manhattan(x, y):
    summation = 0
    for i in range(0, len(x)):
        summation += abs(x[i] - y[i])
    return summation
