def run_k_empty_slots(solution_class: type, bulbs: list[int], k: int):
    implementation = solution_class()
    return implementation.k_empty_slots(bulbs, k)


def assert_k_empty_slots(result: int, expected: int) -> bool:
    assert result == expected
    return True
