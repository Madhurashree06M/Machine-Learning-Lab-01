# Given list = [2,7,4,1,3,6]
# Count pairs of elements with sum = 10

# Brute force approach:
def count_pairs(given_list, length):
    pair_count = 0
    for i in range(0, length):
        for j in range(i+1, length):
            if given_list[i] + given_list[j] == 10: #checking the condition
                pair_count+=1  #finding count of pairs that are meeting the condition

    return pair_count

def main():
    list1 = [2, 7, 4, 1, 3, 6]
    length = len(list1)
    count = count_pairs(list1, length)
    print(f"There are '{count}' pairs of elements that add up to 10")

main()