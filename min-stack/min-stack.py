class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
         

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
    
        # if min stack is empty or this number is smaller than the top of the min stack
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])
            
        # add to the count
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1
        

    def pop(self):
        """
        :rtype: None
        """
        
        # if the top of the min_stack is the same as the top of the stack
        # decrement the count at the top by 1
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
        
        # if the count is 0, pop it out of the min stack
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()