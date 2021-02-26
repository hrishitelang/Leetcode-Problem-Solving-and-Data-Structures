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
    
    def isempty(self):
        return len(self.stack) == 0
    
    def display(self):
        print(self.stack)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        else:
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    stack.push(i)

                elif (i == ')' and stack.peek() == '(') or (i == ']' and stack.peek() == '[') or (i == '}' and stack.peek() == '{'):
                    stack.pop()
                else:
                    stack.push(i)
        
        #stack.display()
        if stack.isempty():
            return True
        else:
            return False