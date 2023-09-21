class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

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


if __name__ == '__main__':
    uncycled_nums = LinkedList()
    for i in range(1, 101):
        uncycled_nums.append(i)
    assert not uncycled_nums.detect_cycle()

    cycled_nums = LinkedList()
    for i in range(1, 101):
        cycled_nums.append(i)
    last_node = cycled_nums.search(100)
    prev_node = cycled_nums.search(50)
    last_node.next = prev_node

    assert cycled_nums.detect_cycle()
