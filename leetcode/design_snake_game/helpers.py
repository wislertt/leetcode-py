def run_design_snake_game(solution_class: type, operations: list[str], inputs: list[list]):
    game = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "SnakeGame":
            game = solution_class(inputs[i][0], inputs[i][1], inputs[i][2])
            results.append(None)
        elif op == "move" and game is not None:
            results.append(game.move(inputs[i][0]))
    return results, game


def assert_design_snake_game(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
