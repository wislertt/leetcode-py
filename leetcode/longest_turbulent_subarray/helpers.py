def run_max_turbulence_size(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.max_turbulence_size(arr)


def assert_max_turbulence_size(result: int, expected: int) -> bool:
    assert result == expected
    return True
