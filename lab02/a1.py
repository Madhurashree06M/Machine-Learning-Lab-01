import pandas as pan
import numpy as num

purchase_data = pan.read_excel("Lab_Session_Data.xlsx", sheet_name = "Purchase data")

X = purchase_data[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
Y = purchase_data["Payment (Rs)"]
print(X)
print(Y)

print("(Dimensionality, Number of vectors): ", X.shape)
print("Rank: ", num.linalg.matrix_rank(X))

# X*c = Y
# c = Xinv * Y
psuedo = num.linalg.pinv(X)
C= num.matmul(psuedo, Y)
print(C)