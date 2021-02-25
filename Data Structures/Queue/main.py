class Queue:
    def __init__(self):
        self.queue = []

    def displayoptions(self):
        while True:
            a = int(input("1. Enqueue\n2. Dequeue\n3. Peek\n4. Size\n5. Display\n6. Is Queue empty?\n7. Exit\nChoose your option: "))
            if a == 1:
                data = int(input("Enter the data:"))
                self.enqueue(data)
            if a == 2:
                try:
                    self.dequeue()
                except IndexError:
                    print('The list is already empty. There is no element to pop.')
            if a == 3:
                try:
                    result = self.peek()
                except IndexError:
                    print('The list is already empty. There is no element to pop.')
                else:
                    print(result)
            if a == 4:
                result = self.size()
                print(result)
            if a == 5:
                self.display()
            if a == 6:
                result = self.isempty()
                print(result)
            if a == 7:
                break

    def enqueue(self, data):
        return self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def isempty(self):
        return self.queue == []

    def display(self):
         print(self.queue)


q = Queue()
q.displayoptions()
