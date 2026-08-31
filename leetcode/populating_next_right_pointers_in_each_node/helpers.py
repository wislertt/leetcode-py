from .solution import Node


def _build_tree(root_list: list[int | None]) -> Node | None:
    if not root_list or root_list[0] is None:
        return None
    root = Node(root_list[0])
    queue: list[Node] = [root]
    i = 1
    while queue and i < len(root_list):
        node = queue.pop(0)
        if i < len(root_list) and root_list[i] is not None:
            val = root_list[i]
            assert val is not None
            node.left = Node(val)
            queue.append(node.left)
        i += 1
        if i < len(root_list) and root_list[i] is not None:
            val = root_list[i]
            assert val is not None
            node.right = Node(val)
            queue.append(node.right)
        i += 1
    return root


def _serialize_next_tree(root: Node | None) -> list[int | None]:
    result: list[int | None] = []
    level_start = root
    while level_start is not None:
        current: Node | None = level_start
        while current is not None:
            result.append(current.val)
            current = current.next
        result.append(None)
        level_start = level_start.left
    return result


def run_connect(solution_class: type, root_list: list[int | None]):
    root = _build_tree(root_list)
    implementation = solution_class()
    connected = implementation.connect(root)
    return _serialize_next_tree(connected)


def assert_connect(result: list[int | None], expected_list: list[int | None]) -> bool:
    assert result == expected_list
    return True
