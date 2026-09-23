# highest occuring character and its occurence count

def character_occurrence(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    count_array = [0]*26

    for i in word:
        index = letters.index(i)
        count_array[index] += 1

    max_count = max(count_array)
    max_index = count_array.index(max_count)

    return letters[max_index], max_count

def main():
    word = "hippopotamus"
    character, count = character_occurrence(word)

    print(f"Highest occurring character: {character}, occurrence count: {count}")

main()