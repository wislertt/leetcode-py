def run_find_content_children(solution_class: type, g: list[int], s: list[int]):
    implementation = solution_class()
    return implementation.find_content_children(g, s)


def assert_find_content_children(result: int, expected: int) -> bool:
    assert result == expected
    return True
