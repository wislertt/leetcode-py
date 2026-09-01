def run_eliminate_maximum(solution_class: type, dist: list[int], speed: list[int]):
    implementation = solution_class()
    return implementation.eliminate_maximum(dist, speed)


def assert_eliminate_maximum(result: int, expected: int) -> bool:
    assert result == expected
    return True
