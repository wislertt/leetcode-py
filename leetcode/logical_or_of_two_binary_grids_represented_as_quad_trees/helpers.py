from .solution import Node


def _construct_quad_tree(grid: list[list[int]]) -> Node:
    """Build the canonical minimal quad-tree for a binary grid."""

    def is_uniform(row: int, col: int, size: int) -> bool:
        first = grid[row][col]
        cells = (grid[r][c] for r in range(row, row + size) for c in range(col, col + size))
        return all(cell == first for cell in cells)

    def build(row: int, col: int, size: int) -> Node:
        if is_uniform(row, col, size):
            return Node(bool(grid[row][col]), True)
        half = size // 2
        return Node(
            False,
            False,
            build(row, col, half),
            build(row, col + half, half),
            build(row + half, col, half),
            build(row + half, col + half, half),
        )

    return build(0, 0, len(grid))


def _quad_tree_to_grid(node: Node, n: int) -> list[list[int]]:
    """Expand a quad-tree into the n * n binary grid it represents."""
    grid = [[0] * n for _ in range(n)]

    def fill(cur: Node, row: int, col: int, size: int) -> None:
        if cur.isLeaf:
            value = int(cur.val)
            for r in range(row, row + size):
                for c in range(col, col + size):
                    grid[r][c] = value
            return
        half = size // 2
        children = (
            (cur.topLeft, row, col),
            (cur.topRight, row, col + half),
            (cur.bottomLeft, row + half, col),
            (cur.bottomRight, row + half, col + half),
        )
        for child, r, c in children:
            if child is not None:
                fill(child, r, c, half)

    fill(node, 0, 0, n)
    return grid


def run_intersect(solution_class: type, grid1: list[list[int]], grid2: list[list[int]]):
    tree1 = _construct_quad_tree(grid1)
    tree2 = _construct_quad_tree(grid2)
    implementation = solution_class()
    root = implementation.intersect(tree1, tree2)
    return _quad_tree_to_grid(root, len(grid1))


def assert_intersect(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
