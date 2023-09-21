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


if __name__ == '__main__':
    linked_nums = LinkedList()
    for i in range(1, 101):
        linked_nums.append(i)
    linked_nums.print()
