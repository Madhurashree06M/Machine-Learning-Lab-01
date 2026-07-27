import numpy as num
import math

def dotpdt(A, B):
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]

    return dot

def vector_length(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * A[i]
    ans = math.sqrt(sum)
    return ans

def main():
    A = [58138, 0, 0, 58, 635] #simply taken the columns: Income, kidhome, teenhome, recency and mntwines for ease of calculation
    B = [46344, 1, 1, 38, 11] 

    print("Dot product from own function: ", dotpdt(A,B))
    print("From builtin: ", num.dot(A,B))\

    print("Length of vectors with euclidean norm own function: ", vector_length(A))
    print("Builtin: ", num.linalg.norm(A))

main()