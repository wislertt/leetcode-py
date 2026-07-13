from .solution import Node


def _serialize_quad_tree(node: Node | None) -> list[list[int]]:
    """Preorder serialization: each node as [isLeaf, val]."""
    if node is None:
        return []
    result: list[list[int]] = [[int(node.isLeaf), int(node.val)]]
    if not node.isLeaf:
        result.extend(_serialize_quad_tree(node.topLeft))
        result.extend(_serialize_quad_tree(node.topRight))
        result.extend(_serialize_quad_tree(node.bottomLeft))
        result.extend(_serialize_quad_tree(node.bottomRight))
    return result


def run_construct(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    root = implementation.construct(grid)
    return _serialize_quad_tree(root)


def assert_construct(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
