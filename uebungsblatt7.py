#---exercise 1---

class MyQueue:
    #constructor starts out with empty list
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        # append new element to END of list
        self.queue.append(element)

    def dequeue(self):
        # only touch list if there are still elements
        if len(self.queue) == 0:
            print("Your queue is already empty")
            return
        else:
            # remove FIRST element
            self.queue.pop(0)

    #override str method
    def __str__(self):
        print("List from first input to last input:")
        # return list as string
        return f"{self.queue}"

Queue = MyQueue()
Queue.enqueue("hello")
Queue.enqueue("how")
Queue.enqueue("are")
Queue.enqueue("you")
Queue.enqueue("doing")
print(Queue)
Queue.dequeue()
print(Queue)

#---exercise 2---
