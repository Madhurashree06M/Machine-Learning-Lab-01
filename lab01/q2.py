#list = [ 5,3,8,1,0,4]
#range = (8-0)
#difference between max and min
#check for list being less than 3 elements, error message

def find_range(given_list): 
    minimum = min(given_list)
    maximum = max(given_list)
    range = maximum - minimum + 1 
    return range


def length_check(given_list, length): #condition check
    if length < 3:
        return "Range determination is not possible."
    else:
        found_range = find_range(given_list)
        return found_range

def main():
    list1 = [5, 3, 8, 1, 0, 4]
    length = len(list1)
    range = length_check(list1, length)
    print(f"Range = {range}")

main()