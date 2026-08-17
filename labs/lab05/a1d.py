# defining swap function for ease:
def swap(given_list, i, j):
    temp = given_list[i]
    given_list[i] = given_list[j]
    given_list[j] = temp



# sorting algorithm 1: Bubble Sort
def BubbleSort(given_list, length):
    for i in range(0, length-1):
        swapped = 0;
        for j in range(0, length-i-1):
            if given_list[j] > given_list[j+1]:
                swap(given_list, j+1, j)
                swapped = 1
        if swapped == 0:
                break

# sorting algo 2: Selection Sort
def SelectionSort(given_list, length):
    for i in range(0, length):
        min = i
        for j in range(i+1, length):
            if given_list[min] > given_list[j]:
                min = j
        swap(given_list, min, i)

# solrting algo 3: Insertion sort
def InsertionSort(given_list, length):
    for i in range(1, length):
        key = given_list[i]
        j = i-1
        while (j>=0) and (given_list[j] > key):
            given_list[j+1] = given_list[j]
            j-=1
        given_list[j+1] = key

            