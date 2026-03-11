import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item

    current = node
    for _ in range(idx - 1):
        current = current.next_item

    node_to_delete = current.next_item
    current.next_item = node_to_delete.next_item

    return node


def print_reversed(head):
    if head is None:
        return
    print_reversed(head.next_item)
    print(head.value)


def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


if __name__ == '__main__':
    if LOCAL:
        test()
    else:
        n = int(input())
        nodes = []
        for _ in range(n):
            nodes.append(Node(input().strip()))

        for i in range(n - 1):
            nodes[i].next_item = nodes[i + 1]

        idx = int(input())

        head = nodes[0]
        new_head = solution(head, idx)

        print_reversed(new_head)
