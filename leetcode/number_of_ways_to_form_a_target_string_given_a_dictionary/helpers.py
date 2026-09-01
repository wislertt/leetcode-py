def run_num_ways(solution_class: type, words: list[str], target: str):
    implementation = solution_class()
    return implementation.num_ways(words, target)


def assert_num_ways(result: int, expected: int) -> bool:
    assert result == expected
    return True
