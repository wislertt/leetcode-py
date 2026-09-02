from collections import deque


class SnakeGame:
    # Time: O(1) per move
    # Space: O(w * h + f) for the snake body and food list
    def __init__(self, width: int, height: int, food: list[list[int]]) -> None:
        self.height = height
        self.width = width
        self.food = food
        self.score = 0
        self.food_idx = 0
        self.snake = deque([(0, 0)])
        self.occupied = {(0, 0)}

    def move(self, direction: str) -> int:
        head_i, head_j = self.snake[0]
        new_i, new_j = head_i, head_j
        if direction == "U":
            new_i -= 1
        elif direction == "D":
            new_i += 1
        elif direction == "L":
            new_j -= 1
        elif direction == "R":
            new_j += 1
        if not (0 <= new_i < self.height and 0 <= new_j < self.width):
            return -1
        if (
            self.food_idx < len(self.food)
            and new_i == self.food[self.food_idx][0]
            and new_j == self.food[self.food_idx][1]
        ):
            self.score += 1
            self.food_idx += 1
        else:
            self.occupied.remove(self.snake.pop())
        if (new_i, new_j) in self.occupied:
            return -1
        self.snake.appendleft((new_i, new_j))
        self.occupied.add((new_i, new_j))
        return self.score
