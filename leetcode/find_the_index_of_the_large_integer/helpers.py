from .solution import ArrayReader


def run_get_index(solution_class: type, arr: list[int]):
    reader = ArrayReader(arr)
    return solution_class().get_index(reader)


def assert_get_index(result: int, expected: int) -> bool:
    assert result == expected
    return True
