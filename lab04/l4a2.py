import pandas as pan
import time

# Gemini results:

def label_encode(data):

    # Extract unique labels and sort them to ensure consistent mapping
    unique_labels = sorted(list(set(data)))
    
    # Create mapping dictionary
    label_to_int = {label: idx for idx, label in enumerate(unique_labels)}
    
    # Encode the data
    encoded_values = [label_to_int[item] for item in data]
    
    return encoded_values, label_to_int


def one_hot_encode(data):
    
    # Extract sorted unique categories for consistent column alignment
    unique_categories = sorted(list(set(data)))
    category_to_index = {category: idx for idx, category in enumerate(unique_categories)}
    
    encoded_matrix = []
    for item in data:
        # Create a zero-filled vector for the current item
        row = [0] * len(unique_categories)
        # Set 1 at the position corresponding to the category
        row[category_to_index[item]] = 1
        encoded_matrix.append(row)
        
    return encoded_matrix, unique_categories


# My code:
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