
#---exercize 1---
def power(a:int,b:int):
    # multiply a with itself recursively until b becomes 1
    if b > 1:
        return a * power(a,b-1)
    # when b reaches/is 1, no need for recursion (anymore)
    elif b == 1:
        return a
    # catching wrong input
    else:
        print("B must be a positive integer")
        return -1

a = 2
b = 10

#print(f"{a}^{b} = {power(a,b)}")


#---exercize 2---

def binary_search(numbers:list,num:int,start:int,end:int):
    #check whether number is in list
    if num in numbers:
        # find the middle between start and end
        middle = int(end-((end-start)/2))
        # if num is exactly at middle, return middle
        if numbers[middle] == num:
            return middle
        # if num is smaller than the value at middle, check below
        elif numbers[middle] > num:
            return binary_search(numbers,num,start,middle-1)
        # if num is bigger than the value at middle, check above
        elif numbers[middle] < num:
            return binary_search(numbers,num,middle+1,end)
    else:
        print(f"{num} is not in the list.")
        return -1

ordered_list = [3,5,6,8,10,11,11,13,16]
x = 8
print(f"You can find an instance of {x} at list-index: {binary_search(ordered_list,x,0,len(ordered_list)-1)}")

