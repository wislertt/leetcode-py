import random

from .solution import Node


def _nary_from_list(vals: list[int | None]) -> Node | None:
    if not vals or vals[0] is None:
        return None
    root = Node(vals[0])
    queue: list[Node] = [root]
    i = 2
    while queue and i < len(vals):
        node = queue.pop(0)
        children: list[Node] = []
        while i < len(vals):
            val = vals[i]
            i += 1
            if val is None:
                break
            child = Node(val)
            children.append(child)
            queue.append(child)
        node.children = children
    return root


def _nary_to_list(root: Node | None) -> list[int | None]:
    if root is None:
        return []
    out: list[int | None] = [root.val, None]
    queue: list[Node] = [root]
    while queue:
        node = queue.pop(0)
        for child in node.children:
            out.append(child.val)
            queue.append(child)
        if queue:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


def _shuffled_nodes(root: Node) -> list[Node]:
    nodes: list[Node] = []
    queue: list[Node] = [root]
    while queue:
        node = queue.pop(0)
        nodes.append(node)
        queue.extend(node.children)
    random.Random(len(nodes) * 31 + 7).shuffle(nodes)
    return nodes


def run_find_root(solution_class: type, root_list: list[int | None]):
    root = _nary_from_list(root_list)
    if root is None:
        return []
    nodes = _shuffled_nodes(root)
    result = solution_class().find_root(nodes)
    return _nary_to_list(result)


def assert_find_root(result: list[int | None], expected_list: list[int | None]) -> bool:
    assert result == expected_list
    return True
