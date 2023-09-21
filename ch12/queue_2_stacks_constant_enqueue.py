class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        while len(self.s1) != 1:
            self.s2.append(self.s1.pop())
        result = self.s1.pop()
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return result


if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 10):
        queue.enqueue(i)
    for _ in range(1, 10):
        print(queue.dequeue())

