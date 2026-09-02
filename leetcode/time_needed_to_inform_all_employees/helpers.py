def run_num_of_minutes(
    solution_class: type, n: int, head_id: int, manager: list[int], inform_time: list[int]
):
    implementation = solution_class()
    return implementation.num_of_minutes(n, head_id, manager, inform_time)


def assert_num_of_minutes(result: int, expected: int) -> bool:
    assert result == expected
    return True
