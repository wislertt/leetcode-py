def run_min_flips_mono_increasing(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_flips_mono_increasing(s)


def assert_min_flips_mono_increasing(result: int, expected: int) -> bool:
    assert result == expected
    return True
