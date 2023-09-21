class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0

    def print(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        self.lenght += 1

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            else:
                current = current.next
        return None

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except AttributeError:
                return False

    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current:
            if current.data == target:
                prev.next = current.next
            prev = current
            current = current.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':
    nums = LinkedList()
    for i in range(1, 101):
        nums.append(i)
    nums.reverse()
    assert not nums.detect_cycle()
    for i in range(100, 10, -1):
        nums.remove(i)
    nums.print()

