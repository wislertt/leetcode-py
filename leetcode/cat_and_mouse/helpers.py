def run_cat_mouse_game(solution_class: type, graph: list[list[int]]):
    implementation = solution_class()
    return implementation.cat_mouse_game(graph)


def assert_cat_mouse_game(result: int, expected: int) -> bool:
    assert result == expected
    return True
