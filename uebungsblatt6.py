#---exercise 1---

def binary_search(numbers:list,num:int):
    # find the middle index (cast as int)
    middle = int((len(numbers))/2)
    # if num is exactly at middle, return middle (this also counts if the list only has one value)
    if numbers[middle] == num:
        return True
    # if list has only one value and that's not "num" return false
    elif len(numbers) == 1:
        return False
    # if num is smaller than the value at middle, check below
    elif numbers[middle] > num:
        # define x as the part of the list to search through
        x = slice(0,middle)
        return binary_search(numbers[x],num)
    # if num is bigger than the value at middle, check above
    elif numbers[middle] < num:
        #define x as the part of the list to search through
        x = slice(middle, len(numbers))
        return binary_search(numbers[x],num)


ordered_list = [3,5,6,8,10,11,11,13,16]
x = 6
#print(binary_search(ordered_list,x))

#---excercise 2---

def bubble_sort(numbers:list):
    bool = True
    while bool:
        bool = False
        for i, x in enumerate(numbers):
            if len(numbers) == i+1:
                break
            elif x < numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                bool = True
    return numbers

unordered_list = [8,4,6,10,3,4,7]

print(bubble_sort(unordered_list))