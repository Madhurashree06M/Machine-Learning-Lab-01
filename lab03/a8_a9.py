import pandas as pan
import numpy as num
import math

def find_mean(given_list, length):
    return (sum(given_list)/length)

def find_variance(given_list, length):
    mean = find_mean(given_list, length)
    sum = 0
    for i in given_list:
        sum += (i-mean)**2
    return sum/length

def find_stddev(given_list, length):
    variance = find_variance(given_list, length)
    ans = math.sqrt(variance)
    return ans

def main():
    data = pan.read_excel("Lab Session Data.xlsx", sheet_name = "marketing_campaign")
    column = data["Recency"].tolist()
    length = len(column)
    print("mean with own function: ", find_mean(column, length))
    print("builtin in mean: ", num.mean(column))
    print("variance: ", find_variance(column, length))
    print("std deviation: ", find_stddev(column, length))
    print("builtin in std dev: ", num.std(column))

main()