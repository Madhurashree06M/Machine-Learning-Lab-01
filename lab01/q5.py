# generate list of 25 random numbers between 1 and 10
# find mean median mode
import random
def is_even(length):
    if length % 2 == 0:
        return True
    else:
        return False
     
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

def find_mean(given_list, length):
    return (sum(given_list)/length)

def main():
    random_numbers = [] 
    for i in range(25):
        random_numbers.append(random.randint(1,10))
    print(random_numbers)

    length = len(random_numbers)
    mean = find_mean(random_numbers, length)
    median = find_median(random_numbers, length)
    mode = find_mode(random_numbers, length)

    print(f"Mean: {mean} \nMedian: {median} \nMode: {mode}")

main()