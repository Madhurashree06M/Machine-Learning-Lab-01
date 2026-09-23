# Data Imputation: Missing values of data to be filled in with appropriate central tendencies
# (Mean, Median & Mode)

def is_even(length):
    if length % 2 == 0:
        return True
    else:
        return False

def find_mean(given_list):
    sum=0
    for i in given_list:
        sum+= i
    return sum / len(given_list)

def find_median(given_list, length):
    sorted_list = sorted(given_list)
    if is_even(length) == True:
        return (sorted_list[length//2 - 1] + sorted_list[length//2])/2
    else:
        return sorted_list[length//2] 

def find_mode(given_list, length):
    minimum = min(given_list)
    maximum = max(given_list)
    range = maximum - minimum + 1

    count_array = [0]*range
    for num in given_list:
        count_array[num-1] += 1
    
    max_count = max(count_array)
    mode = count_array.index(max_count) + 1

    return mode