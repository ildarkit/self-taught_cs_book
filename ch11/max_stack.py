class MaxStack():
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]


if __name__ == '__main__':
    max_stack = MaxStack()
    max_stack.push(7)
    max_stack.push(15)
    max_stack.push(7)
    max_stack.push(4)
    max_stack.push(0)
    max_stack.push(12)
    assert max_stack.get_max() == 15
