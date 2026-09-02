class Robot:
    # Test-harness API: backs the interactive move/turn/clean interface with the grid
    def __init__(self, room: list[list[int]], row: int, col: int) -> None:
        self.room = room
        self.row = row
        self.col = col
        self.direction = 0  # 0 up, 1 right, 2 down, 3 left
        self.cleaned: set[tuple[int, int]] = set()

    def move(self) -> bool:
        dr = (-1, 0, 1, 0)[self.direction]
        dc = (0, 1, 0, -1)[self.direction]
        nr, nc = self.row + dr, self.col + dc
        if (
            nr < 0
            or nr >= len(self.room)
            or nc < 0
            or nc >= len(self.room[0])
            or self.room[nr][nc] == 0
        ):
            return False
        self.row, self.col = nr, nc
        return True

    def turn_left(self) -> None:
        self.direction = (self.direction + 3) % 4

    def turn_right(self) -> None:
        self.direction = (self.direction + 1) % 4

    def clean(self) -> None:
        self.cleaned.add((self.row, self.col))


class Solution:
    # Time: O(m * n)
    # Space: O(m * n) visited set
    def clean_room(self, robot: Robot) -> None:
        deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
        visited: set[tuple[int, int]] = set()

        def go_back() -> None:
            robot.turn_right()
            robot.turn_right()
            robot.move()
            robot.turn_right()
            robot.turn_right()

        def backtrack(cell: tuple[int, int], direction: int) -> None:
            visited.add(cell)
            robot.clean()
            for k in range(4):
                nd = (direction + k) % 4
                ncell = (cell[0] + deltas[nd][0], cell[1] + deltas[nd][1])
                if ncell not in visited and robot.move():
                    backtrack(ncell, nd)
                    go_back()
                robot.turn_right()

        backtrack((0, 0), 0)
