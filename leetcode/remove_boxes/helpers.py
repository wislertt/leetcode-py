def run_remove_boxes(solution_class: type, boxes: list[int]):
    implementation = solution_class()
    return implementation.remove_boxes(boxes)


def assert_remove_boxes(result: int, expected: int) -> bool:
    assert result == expected
    return True
