import pandas as pan
import math

# Nominal -> One-hot encoding
# Ordinal -> Label encoding 

# encoding: Label encoding
def label_encoding(given_column): # own function 
    unique_stuff = given_column.unique()
    mapping = {}
    number = 0
    for i in unique_stuff:
        mapping[i] = number
        number += 1

    label_encoded = []
    for i in given_column:
        label_encoded.append(mapping[i])

    return label_encoded, mapping

def onehot_encoding(given_column): # own function
    unique_stuff = given_column.unique()

    encoded = {}

    for i in unique_stuff:
        encoded[i]=[]

    for i in given_column:
        for j in unique_stuff:
            if i == j:
                encoded[j].append(1)
            else:
                encoded[j].append(0)

    return pan.DataFrame(encoded)






