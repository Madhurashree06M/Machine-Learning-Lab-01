# gemini code
def minkowski_distance(x, y, p=2):

    if len(x) != len(y):
        raise ValueError("Both vectors must have the same dimensions.")
    
    if p < 1:
        raise ValueError("Order parameter p must be greater than or equal to 1.")
        
    # Calculate the generalized distance
    distance = sum(abs(a - b) ** p for a, b in zip(x, y)) ** (1 / p)
    
    return distance

# my code: 
from scipy.spatial.distance import minkowski as minkow
def minkowski(x, y, p): # own function
    summation = 0
    for i in range(len(x)):
        summation += (x[i]-y[i])**p # formula given in sheet

    dist = summation ** (1/p)
    return dist


def main():
    x = [58138, 0, 0, 58, 635] 
    y = [46344, 1, 1, 38, 11] 

    for p in range(1, 11):
        print("p = ", p)
        print("gemini function distance = ", minkowski_distance(x,y,p))
        print("own function distance = ", minkowski(x,y,p))
        print("builtin calculation = ", minkow(x,y,p))
    
main()
