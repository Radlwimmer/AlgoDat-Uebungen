#---exercize 1---

def binary_search(numbers:list,num:int):
    # find the middle index (cast as int, rounded up)
    middle = int((len(numbers)+1)/2)
    # if num is exactly at middle, return middle
    if numbers[middle] == num:
        return true
    # if num is smaller than the value at middle, check below
    elif numbers[middle] > num:
        # define x as the part of the list to search through
        x = slice(0,middle-1)
        return binary_search(numbers[x],num)
    # if num is bigger than the value at middle, check above
    elif numbers[middle] < num:
        #define x as the part of the list to search through
        x = slice(middle, len(numbers)-1)
        return binary_search(numbers[x],num)
    else:
        print(f"{num} is not in the list.")
        return -1

ordered_list = [3,5,6,8,10,11,11,13,16]
x = 8
print(binary_search(ordered_list,x))
middle = int((len(ordered_list)+1)/2)
x = slice(middle,len(ordered_list))
print(ordered_list[x])

