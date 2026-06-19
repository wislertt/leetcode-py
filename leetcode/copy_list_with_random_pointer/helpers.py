from .solution import Node


def _build_random_list(nodes: list[list[int | None]]) -> Node | None:
    if not nodes:
        return None
    created: list[Node] = []
    for node_spec in nodes:
        val = node_spec[0]
        assert isinstance(val, int)
        created.append(Node(val))
    for i, node_spec in enumerate(nodes):
        if i + 1 < len(created):
            created[i].next = created[i + 1]
        rand_idx = node_spec[1]
        if rand_idx is not None:
            created[i].random = created[rand_idx]
    return created[0]


def _serialize_random_list(head: Node | None) -> list[list[int | None]]:
    index_by_id: dict[int, int] = {}
    cur: Node | None = head
    i = 0
    while cur is not None:
        index_by_id[id(cur)] = i
        i += 1
        cur = cur.next
    result: list[list[int | None]] = []
    cur = head
    while cur is not None:
        rand_idx = index_by_id[id(cur.random)] if cur.random is not None else None
        result.append([cur.val, rand_idx])
        cur = cur.next
    return result


def run_copy_random_list(solution_class: type, nodes: list[list[int | None]]):
    implementation = solution_class()
    head = _build_random_list(nodes)
    copied = implementation.copy_random_list(head)
    return _serialize_random_list(copied)


def assert_copy_random_list(
    result: list[list[int | None]], expected: list[list[int | None]]
) -> bool:
    assert result == expected
    return True
