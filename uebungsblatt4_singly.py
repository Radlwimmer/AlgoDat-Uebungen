# Class implementation of a singly linked list convention head -> tail
# Node class holds the data and the pointer to the next object
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Class for managing the list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    #Overwriting the iteration function with a generator function to make iteration over elements possible
    def __iter__(self):
        current=self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size



#############################################################################################
# Exercise Part #############################################################################
    def show_data(self):
        for i in self.__iter__():
            print(i)

    def clear(self):
        if self.head == None:
            print("Your list is already empty")
            return
        else:
            self.head = None
            self.size = 0
        return

    def search(self, data):
        for i in self.__iter__():
            if i == data:
                return True
        return False

    def delete(self, data):
        if self.head == None:
            print("Your list is empty, no data to delete")
            return
        else:
            current = self.head
            while current.data is not data:
                prev = current
                current = current.next
            if current.next is not None:
                current.data = current.next.data
                current.next = current.next.next
            else:
                prev.next = None
            self.size -= 1
            print(f"The first occurrence of \"{data}\" has been deleted from the list")

        return


if __name__ == '__main__':
    print("Exercise 4")

Test = SinglyLinkedList()
Test.append(1)
Test.append(2)
Test.append(3)
Test.append(4)
Test.append(5)
Test.show_data()
Test.delete(5)
Test.show_data()
Test.append(6)
Test.show_data()
Test.delete(6)
Test.show_data()




