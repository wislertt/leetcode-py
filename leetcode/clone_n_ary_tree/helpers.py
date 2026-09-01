from .solution import NaryNode


def _nary_nodes(root: NaryNode | None) -> list[NaryNode]:
    if root is None:
        return []
    out: list[NaryNode] = []
    stack: list[NaryNode] = [root]
    while stack:
        node = stack.pop()
        out.append(node)
        stack.extend(node.children)
    return out


def _nary_from_list(vals: list[int | None]) -> NaryNode | None:
    if not vals:
        return None
    v0 = vals[0]
    assert v0 is not None
    root = NaryNode(v0)
    queue: list[NaryNode] = [root]
    i = 2
    while queue:
        node = queue.pop(0)
        while i < len(vals) and vals[i] is not None:
            v = vals[i]
            assert v is not None
            child = NaryNode(v)
            node.children.append(child)
            queue.append(child)
            i += 1
        i += 1
    return root


def _nary_to_list(root: NaryNode | None) -> list[int | None]:
    if root is None:
        return []
    out: list[int | None] = [root.val, None]
    queue: list[NaryNode] = [root]
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


def run_clone_tree(solution_class: type, root_list: list[int | None]):
    root = _nary_from_list(root_list)
    clone = solution_class().clone_tree(root)
    for node in _nary_nodes(root):
        node.children = []
    return clone


def assert_clone_tree(result: NaryNode | None, expected_list: list[int | None]) -> bool:
    assert _nary_to_list(result) == expected_list
    return True
