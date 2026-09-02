def run_max_boxes_in_warehouse(solution_class: type, boxes: list[int], warehouse: list[int]):
    implementation = solution_class()
    return implementation.max_boxes_in_warehouse(boxes, warehouse)


def assert_max_boxes_in_warehouse(result: int, expected: int) -> bool:
    assert result == expected
    return True
