def run_min_operations(solution_class: type, boxes: str):
    implementation = solution_class()
    return implementation.min_operations(boxes)


def assert_min_operations(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
