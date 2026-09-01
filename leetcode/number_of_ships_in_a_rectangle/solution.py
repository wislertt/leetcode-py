class Point:
    # Test-harness value type for a cartesian point on the sea
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Sea:
    # Test-harness API: backs the interactive has_ships query with the ships
    def __init__(self, ships: list[list[int]]) -> None:
        self.ships = {(x, y) for x, y in ships}
        self.calls = 0

    def has_ships(self, top_right: Point, bottom_left: Point) -> bool:
        self.calls += 1
        if self.calls > 400:
            msg = "has_ships exceeded the 400-call judge limit"
            raise RuntimeError(msg)
        return any(
            bottom_left.x <= x <= top_right.x and bottom_left.y <= y <= top_right.y
            for x, y in self.ships
        )


class Solution:
    # Time: O(C * log(max(m, n))) API calls, C = ships inside the rectangle
    # Space: O(log(max(m, n))) recursion
    def count_ships(self, sea: Sea, top_right: Point, bottom_left: Point) -> int:
        def dfs(tr: Point, bl: Point) -> int:
            x1, y1 = bl.x, bl.y
            x2, y2 = tr.x, tr.y
            if x1 > x2 or y1 > y2:
                return 0
            if not sea.has_ships(tr, bl):
                return 0
            if x1 == x2 and y1 == y2:
                return 1
            midx = (x1 + x2) // 2
            midy = (y1 + y2) // 2
            return (
                dfs(tr, Point(midx + 1, midy + 1))
                + dfs(Point(midx, y2), Point(x1, midy + 1))
                + dfs(Point(midx, midy), bl)
                + dfs(Point(x2, midy), Point(midx + 1, y1))
            )

        return dfs(top_right, bottom_left)
