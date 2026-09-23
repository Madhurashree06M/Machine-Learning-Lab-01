#square matrix A and positive integer m
#returns A^m

def multiply(A1, A2, length):
    result = [[0]* length for i in range(length)] #list comprehension to make matrix result 
    for i in range(length): #row
        for j in range(length): #column
            for k in range(length): #compute
                result[i][j] += A1[i][k] * A2[k][j] #matric multiplication logic
    return result

def power(A, length, m):
    result = [[0]* length for i in range(length)] #list comprehension
    for i in range(length):
        result[i][i] = 1
    
    for i in range(m):
        result = multiply(result, A, length)
    
    return result

def main():
    A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    length = len(A)
    m = 3
    result = power(A, length, m)
    for i in result:
        print(i)

main()
