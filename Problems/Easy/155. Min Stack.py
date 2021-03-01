"""

155. Min Stack

Each element in this stack consists of two values, the first being the number itself, and the second being the smallest number
seen till the current element in the stack. To get the smallest element all we need to do is return the second value.
"""

class MinStack:

    def __init__(self):
        self.data = []
        

    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append([x,x])
        else:
            topElement = self.data[-1]
            print(topElement)
            self.data.append([x,min(x,topElement[1])])
        
    def pop(self) -> None:
        self.data.pop()
        
    def top(self) -> int:
        return self.data[-1][0]
    
    def getMin(self) -> int:
        return self.data[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()