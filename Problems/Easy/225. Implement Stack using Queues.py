"""

225. Implement Stack using Queues

Instead of using Python' Collection's Queue, I have implemented my own below.
The working is simple enough for anyone to understand.

Notes:
I believe the only tricky function is my implementation of pop.
1) I have two pointers, one called currentQueue and the other is otherQueue.
2) When I need to perform the pop operation, I set currentQueue to the queue with all the elements and otherQueue to the empty queue.
I pop all but one element from currentQueue and push them into otherQueue, save the element I need to return (first element in currentQueue) and
interchange the pointers for currentQueue and otherQueue. Now currentQueue should point to the queue with the elements and otherQueue
should point to the empty queue.
This happens everytime we need to pop an element.

"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()
        self.currentQueue = self.queue1
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.currentQueue.push(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.currentQueue.isEmpty():
            raise Exception
        else:
            if self.currentQueue is self.queue1:
                self.otherQueue = self.queue2
            else:
                self.otherQueue = self.queue1
            while self.currentQueue.size() > 1:
                self.otherQueue.push(self.currentQueue.pop())
            element = self.currentQueue.queue[0]
            self.currentQueue.queue = self.currentQueue.queue[1:]
            self.currentQueue, self.otherQueue = self.otherQueue, self.currentQueue
            return element
            

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.currentQueue.isEmpty():
            raise Exception
        else:
            element = self.pop()
            self.push(element)
            return element

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.currentQueue.queue) == 0

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.isEmpty():
            element = self.queue[0]
            self.queue = self.queue[1:]
            return element
        else:
            raise Exception("The queue is empty")
        

    def size(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return len(self.queue)

    def isEmpty(self) -> bool:
        """
        Returns whether the queue is empty
        """
        return len(self.queue) == 0

        
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
param_2 = obj.pop()
# param_3 = obj.top()
param_4 = obj.empty()

# obj = MyQueue()
# obj.push(5)
# obj.push(4)
# obj.push(3)
# obj.push(2)
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.size())
# print(obj.isEmpty())
