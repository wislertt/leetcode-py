def run_reconstruct_queue(solution_class: type, people: list[list[int]]):
    implementation = solution_class()
    return implementation.reconstruct_queue(people)


def assert_reconstruct_queue(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
