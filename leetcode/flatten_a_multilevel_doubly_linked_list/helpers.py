class MlNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.prev: MlNode | None = None
        self.next: MlNode | None = None
        self.child: MlNode | None = None


def ml_from_list(vals: list[int | None]) -> MlNode | None:
    pos = 0

    def parse_level() -> MlNode | None:
        nonlocal pos
        nodes: list[MlNode] = []
        while pos < len(vals) and vals[pos] is not None:
            v = vals[pos]
            assert v is not None
            nodes.append(MlNode(v))
            pos += 1
        for i, node in enumerate(nodes):
            if i > 0:
                node.prev = nodes[i - 1]
                nodes[i - 1].next = node
        if pos < len(vals) and vals[pos] is None:
            pos += 1
        for node in nodes:
            if pos >= len(vals):
                break
            if vals[pos] is None:
                pos += 1
            else:
                node.child = parse_level()
        return nodes[0] if nodes else None

    return parse_level()


def ml_to_list(head: MlNode | None) -> list[int]:
    out: list[int] = []
    node = head
    while node is not None:
        assert node.child is None
        if out:
            assert node.prev is not None
        else:
            assert node.prev is None
        out.append(node.val)
        node = node.next
    return out


def run_flatten(solution_class: type, head_list: list[int | None]):
    head = ml_from_list(head_list)
    implementation = solution_class()
    return ml_to_list(implementation.flatten(head))


def assert_flatten(result: list[int], expected_list: list[int | None]) -> bool:
    assert result == expected_list
    return True
