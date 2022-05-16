from node import Node


def printList(head):
    while head is not None:
        print(head.value)
        head = head.nxt


if __name__ == "__main__":
    n1 = Node(10, None)
    n2 = Node(20, n1)
    n3 = Node(30, n2)

    printList(n3)
