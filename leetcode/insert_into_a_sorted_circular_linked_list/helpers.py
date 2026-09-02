from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, next: Node | None = None) -> None:
        self.val = val
        self.next = next


def run_insert(solution_class: type, head_list: list[int], insert_val: int):
    if not head_list:
        head = None
    else:
        nodes = [Node(v) for v in head_list]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = nodes[0]
        head = nodes[0]
    implementation = solution_class()
    return implementation.insert(head, insert_val)


def assert_insert(result: Node, expected_list: list[int]) -> bool:
    assert result is not None
    vals: list[int] = []
    node: Node = result
    while True:
        vals.append(node.val)
        nxt = node.next
        if nxt is None:
            raise AssertionError
        node = nxt
        if node is result:
            break
    assert vals == expected_list
    return True
