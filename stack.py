class stack:
    top = -1

    def __init__(self, top=0):
        self.list = []
        self.top = top

    def push(self, data):
        self.top = self.top + 1
        self.list.append(data)

    def pop(self):
        if self.top == 0:
            print("Stack is empty.")
            return

        self.top = self.top - 1
        return self.list.pop()

    def display(self):
        print(self.list)

    def peek(self):
        print(self.list[self.top])


s = stack()
# s.push("a")
# s.push("a")
# s.push("a")
# s.push("a")
print((s.pop()))

s.display()
