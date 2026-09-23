import pandas as pan

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

def recreate_dataset(original): #Categorical features = Nominal and Ordinal
# marital status = nominal, education = ordinal
    working_df = original.copy()

    education_encoded, education_mapping = label_encoding(working_df["Education"])
    working_df["Education"] = education_encoded

    marital_onehot = onehot_encoding(working_df["Marital_Status"])
    marital_onehot.columns = ["Marital_" + str(col) for col in marital_onehot.columns]

    working_df = working_df.drop(columns=["Marital_Status"])
    working_df = pan.concat([working_df, marital_onehot], axis = 1)

    return working_df, education_mapping

def main():
    data = pan.read_excel("Lab Session Data.xlsx", sheet_name = "marketing_campaign")
    new_df, education_map = recreate_dataset(data)

    print("Education label mapping:", education_map)
    print("Original dimensionality:", data.shape[1]) # index = 1 shows no. of columns
    print("simensionality after encoding:", new_df.shape[1])

main()