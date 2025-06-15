ids_list = [10, 20, 30, 40, 50]

def negativeIndex(my_list):
    last_item = my_list[-1]
    one_before_last_item = my_list[-2]
    print("Last item is " + str(last_item) + ", One before that is " + str(one_before_last_item))

def lastIndexWithLen(my_list):
    print("The list len is " + str(len(my_list)) + ", so the last index is " + str(len(my_list)) + " - 1, which is " + str(len(my_list) - 1))
    print(my_list[len(my_list) - 1])

def slicing(my_list):
    return my_list[:]

def regularVarPointer():
    number = 20
    copy_of_number = number
    copy_of_number += 1
    print(number)
    print(copy_of_number)

def listPointer():
    my_list = [1, 2, 3]
    copy_of_my_list = my_list
    copy_of_my_list.append(200)
    print(my_list)
    print(copy_of_my_list)

def listCopy():
    my_list = [1, 2, 3]
    copy_of_my_list = my_list[:]
    copy_of_my_list.append(200)
    print(my_list)
    print(copy_of_my_list)

def addNumberToList(my_list, number):
    my_list.append(number)

def sorting():
    my_list = [200, 80, 90, 45, 70, 1]
    my_list.sort()
    print(my_list)
    my_list.sort(reverse=True)
    print(my_list)
    # my_list.append("abcd")
    # my_list.sort()
    
def countUserWords():
    text = input("Write down some words: ")
    words = text.split()
    words.sort()
    print("Sorted words is " + str(words))
    print("There are " + str(len(words)) + " words")

def add_item(my_list, item):
    print_all(my_list, item)

def print_all(original_list, new_item_string):
    # Display a sorted list and reverse order
    sorted_list = sorted(original_list)
    reversed_sorted_list = sorted(original_list, reverse=True)
    print("Sorted list:", sorted_list)
    print("Reversed sorted list:", reversed_sorted_list)

    # Maximum and minimum
    print("Max number in list:", max(original_list))
    print("Min number in list:", min(original_list))

    # Five Max numbers
    print("Top 5 numbers:", find_top_5_numbers(original_list))

    # Convert from a string to a list of integers
    item_list = list(map(int, new_item_string.split("|")))
    sorted_item_list = sorted(item_list)
    print("Sorted new items:", sorted_item_list)

def find_top_5_numbers(lst):
    return sorted(lst, reverse=True)[:5]

# Calling the code
my_list1 = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
item1 = "16|11|20|-2|9|19|7|5|10|5|20|-9|16|7|4|2|-5|2|-3|10"
add_item(my_list1, item1)
