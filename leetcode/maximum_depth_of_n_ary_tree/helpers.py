from .solution import NaryNode


def _nary_from_list(vals: list[int | None]) -> NaryNode | None:
    """Build an n-ary tree from LeetCode level-order form (None separates child groups)."""
    if not vals or vals[0] is None:
        return None
    root = NaryNode(vals[0])
    queue: list[NaryNode] = [root]
    i = 2
    while queue and i < len(vals):
        node = queue.pop(0)
        children: list[NaryNode] = []
        while i < len(vals):
            val = vals[i]
            i += 1
            if val is None:
                break
            child = NaryNode(val)
            children.append(child)
            queue.append(child)
        node.children = children
    return root


def run_max_depth(solution_class: type, root_list: list[int | None]):
    root = _nary_from_list(root_list)
    implementation = solution_class()
    return implementation.max_depth(root)


def assert_max_depth(result: int, expected: int) -> bool:
    assert result == expected
    return True
