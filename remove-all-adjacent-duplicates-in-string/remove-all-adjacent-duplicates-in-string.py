class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        return self.stack.append(data)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
        
    def display(self):
        return self.stack
    
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = Stack()
        for i in S:
            if stack.peek() != i:
                stack.push(i)
            else:
                stack.pop()
        return "".join(stack.display())