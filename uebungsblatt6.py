ordered_list = [3,5,6,8,10,11,11,13,16]
unordered_list = [8,4,6,10,3,4,7,25]

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



x = 6
#print(binary_search(ordered_list,x))

#---excercise 2---

def bubble_sort(numbers:list):
    #set condition for while loop (do while)
    bool = True
    while bool:
        # set loop to terminate unless something happens (if there was no swap necessary in the last round, the list is ordered and the loop terminates)
        bool = False
        # loop through the list
        for i, x in enumerate(numbers):
            # stop loop at last value
            if len(numbers) == i+1:
                break
            # if first number is smaller than second number swap them
            elif x < numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                # set loop condition true, so algorithm checks list again
                bool = True
    return numbers

#print(bubble_sort(unordered_list))

#---excercise 3---

def insertions_sort(numbers:list):
    #set loop for element to be sorted
    for i, x in enumerate(numbers):
        #set loop for elements to compare it with
        for j, y in enumerate(numbers):
            #only compare to elements that have already been sorted
            if j == i:
                break
                #if an element is out of order:
            elif numbers[i] > numbers[j]:
                # insert it before the other element
                numbers.insert(j,numbers[i])
                # and remove it from the other position
                numbers.pop(i+1)
                # and don't compare it to other elements
                break
    return numbers

#print(insertions_sort(unordered_list))

#---excercise 4---
#Hash tables with hash buckets are basically arrays with linked lists

class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class HashList():
    def __init__(self, size=None):
        self.size = size
        self.bucket = self.size * [None]

    def insert(self, element:str):
        node = Node(element)
        if self.bucket[len(element) % 10] == None:
            self.bucket[len(element) % 10] = node
        else:
            current = self.bucket[len(element) % 10]
            while current.next:
                current = current.next
            current.next = node


    def show_content(self):
        for i in range(self.size):
            print(i, end=' ')
            current = self.bucket[i]
            while current:
                val = current.data
                print(val, end=' ')
                current = current.next
            print()



hashtable = HashList(10)
hashtable.insert("Eier")
hashtable.insert("Milch")
hashtable.insert("Mehl")
hashtable.insert("Erdaepfel")
hashtable.insert("Schlagobers")
hashtable.insert("Eis")
hashtable.insert("Bananen")
hashtable.show_content()



