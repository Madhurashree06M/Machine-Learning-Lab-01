# gemini's code: 

import pandas as pd
import numpy as np

def calculate_mean(data):
    """Calculates the arithmetic mean of a list/sequence of numbers."""
    clean_data = [x for x in data if pd.notna(x)]
    if not clean_data:
        return None
    return sum(clean_data) / len(clean_data)

def calculate_variance(data, ddof=1):
    """
    Calculates the variance of a list/sequence of numbers.
    ddof=1 calculates Sample Variance (unbiased).
    """
    clean_data = [x for x in data if pd.notna(x)]
    n = len(clean_data)
    if n <= ddof:
        return None
    mean_val = calculate_mean(clean_data)
    return sum((x - mean_val) ** 2 for x in clean_data) / (n - ddof)

def calculate_std(data, ddof=1):
    """Calculates the standard deviation of a list/sequence of numbers."""
    var_val = calculate_variance(data, ddof=ddof)
    if var_val is None:
        return None
    return var_val ** 0.5

def analyze_marketing_campaign(file_path, sheet_name='marketing_campaign'):
    """
    Reads the dataset sheet and computes Mean, Variance, 
    and Standard Deviation for all numerical features.
    """
    # Load dataset
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Select numerical columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    results = []
    for col in numeric_cols:
        col_data = df[col].dropna().tolist()
        
        mean_val = calculate_mean(col_data)
        var_val = calculate_variance(col_data)
        std_val = calculate_std(col_data)
        
        results.append({
            'Feature': col,
            'Mean': mean_val,
            'Variance': var_val,
            'Std Dev': std_val
        })
        
    return pd.DataFrame(results)

# --- Run Analysis ---
file_path = 'Lab Session Data.xlsx'
summary_df = analyze_marketing_campaign(file_path)
print(summary_df)



# MY CODE:  
# import pandas as pan
# import numpy as num
# import math

# def find_mean(given_list, length):
#     return (sum(given_list)/length)

# def find_variance(given_list, length):
#     mean = find_mean(given_list, length)
#     sum = 0
#     for i in given_list:
#         sum += (i-mean)**2
#     return sum/length

# def find_stddev(given_list, length):
#     variance = find_variance(given_list, length)
#     ans = math.sqrt(variance)
#     return ans

# def main():
#     data = pan.read_excel("Lab Session Data.xlsx", sheet_name = "marketing_campaign")
#     column = data["Recency"].tolist()
#     length = len(column)
#     print("mean with own function: ", find_mean(column, length))
#     print("builtin in mean: ", num.mean(column))
#     print("variance: ", find_variance(column, length))
#     print("std deviation: ", find_stddev(column, length))
#     print("builtin in std dev: ", num.std(column))

# main()

