class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        return self.stack.append(data)
        
    def pop(self):
        return self.stack.pop()
        
    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            return 0
    
    def display(self):
        print(self.stack)
        
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        stack = Stack()
        for i in s:
            if i == "I":
                number += 1
            if i == "V":
                if stack.top() == "I":
                    number += 4
                    number -= 1
                else:
                    number += 5
            if i == "X":
                if stack.top() == "I":
                    number += 9
                    number -= 1
                else:
                    number += 10      
            if i == "L":
                if stack.top() == "X":
                    number += 40
                    number -= 10
                else:
                    number += 50
            if i == "C":
                if stack.top() == "X":
                    number += 90
                    number -= 10
                else:
                    number += 100
            if i == "D":
                if stack.top() == "C":
                    number += 400
                    number -= 100
                else:
                    number += 500
            if i == "M":
                if stack.top() == "C":
                    number += 900
                    number -= 100
                else:
                    number += 1000
            stack.push(i)
            stack.display()
            print(stack.top())
        return number