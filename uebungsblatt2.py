import array as arr
import copy

#declarations
my_array = arr.array('i',[6,6,7,7,7,8])
my_list=[6,6,7,7,7,8]
my_text=['eeny','meeny','eeny','miny','eeny','moe','moe']
my_dictionary={'Price':'1000€'}

#functions
#exercise 1
def count_integer(numbers:arr,integer:int):
    count = 0

    for i in numbers:
        if i == integer:
            count += 1
    return count


#exercise 2
def array_func(numbers:arr,integer:int):
    rev = copy.deepcopy(numbers)
    rev.reverse()
    print(f"Original array: {numbers}")
    print(f"Reversed array: {rev}")

    if numbers.count(integer) == 0:
        print(f"{integer} is not an element of the array.")
    else:
        print("\nNumbers to be removed from array:")
        for i, val in enumerate(numbers):
            if val == integer:
                print(f"Number:{val}\t Index: {i}")
        while numbers.count(integer) > 0:
            numbers.remove(integer)
        print(f"Shortened array: {numbers}")

#exercise 3
def list_func(numbers:list,integer:int):
    rev = copy.deepcopy(numbers)
    rev.reverse()
    print(f"Original list: {numbers}")
    print(f"Reversed list: {rev}")

    for i, val in enumerate(numbers):
        if val == integer:
            numbers[i] = 1
    print(f"Edited list: {numbers}")
    print(f"From highest to lowest number:{sorted(numbers,reverse=True)}")

#exercise 4
def remove_duplicates(text:list):
    text = list(dict.fromkeys(text))
    return text

#exercise 5
#getdefault verwenden
def dict_func(dictionary:dict):
    x = dictionary.setdefault('Type', 'unknown item')
    x = dictionary.setdefault('Brand', 'an unknown brand')
    x = dictionary.setdefault('Price', 'an unknown price')
    x = dictionary.setdefault('OS', 'Linux')
    print(f"You have a(n) {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}.")
    print(f"Your operating system is: {dictionary['OS']}.")
    print(dictionary)


#main
#exercise 1
#print(count_integer(my_array, 7))
#exercise 2
#array_func(my_array,7)
#exercise 3
#list_func(my_list,7)
#exercise 4
#print(remove_duplicates(my_text))
#exercise 5
#dict_func(my_dictionary)

