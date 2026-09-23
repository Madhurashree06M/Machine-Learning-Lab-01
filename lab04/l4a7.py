import numpy as num

# gemini's code:

import math

def dot_product(A, B):

    if len(A) != len(B):
        raise ValueError("Vectors A and B must have the same dimension.")
    
    return sum(a * b for a, b in zip(A, B))


def euclidean_norm(vector):
    """
    Calculates the length (Euclidean / L2 Norm) of a vector.
    
    Parameters:
    vector (iterable): The input vector.
    
    Returns:
    float: The Euclidean length of the vector.
    """
    return math.sqrt(sum(x ** 2 for x in vector))


# MY CODE: 
# import numpy as num
# import math

# def dotpdt(A, B):
#     dot = 0
#     for i in range(len(A)):
#         dot += A[i] * B[i]

#     return dot

# def vector_length(A):
#     sum = 0
#     for i in range(len(A)):
#         sum += A[i] * A[i]
#     ans = math.sqrt(sum)
#     return ans


def main():
    A = [58138, 0, 0, 58, 635] #simply taken the columns: Income, kidhome, teenhome, recency and mntwines for ease of calculation
    B = [46344, 1, 1, 38, 11] 

    print("Dot product from own function: ", dot_product(A,B))
    print("From builtin: ", num.dot(A,B))\

    print("Length of vectors with euclidean norm own function: ", euclidean_norm(A))
    print("Builtin: ", num.linalg.norm(A))

main()