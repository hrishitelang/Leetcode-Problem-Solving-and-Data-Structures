class Stack:
    def __init__(self):
        self.stack = []

    def displayoptions(self):
        while True:
            a = int(input("Choose options:\n1. Push\n2. Pop\n3.Peek\n4. Size\n5. Display\n6. Exit\n"))
            if a == 1:
                data = int(input("Enter data:"))
                self.push(data)
            if a == 2:
                result = self.pop()
                print(f"Element {result} popped")
            if a == 3:
                result = self.peek()
                print(result)
            if a == 4:
                result = self.size()
                print(result)
            if a == 5:
                result = self.display()
                print(result)
            if a == 6:
                break

    def push(self, data):
        return self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack

stack = Stack()
stack.displayoptions()