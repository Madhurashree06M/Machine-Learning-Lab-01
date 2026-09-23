from scipy.spatial.distance import minkowski as minkow
def minkowski(x, y, p): # own function
    summation = 0
    for i in range(len(x)):
        summation += (x[i]-y[i])**p # formula given in sheet

    dist = summation ** (1/p)
    return dist

def main():
    x = [58138, 0, 0, 58, 635] #simply taken the columns: Income, kidhome, teenhome, recency and mntwines for ease of calculation
    y = [46344, 1, 1, 38, 11] 

    for p in range(1, 11):
        print("p = ", p)
        print("own function distance = ", minkowski(x,y,p))
        print("builtin calculation = ", minkow(x,y,p))
    
main()