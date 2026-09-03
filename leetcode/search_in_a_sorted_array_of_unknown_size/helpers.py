from .solution import ArrayReader


def run_search(solution_class: type, secret: list[int], target: int):
    reader = ArrayReader(secret)
    return solution_class().search(reader, target)


def assert_search(result: int, expected: int) -> bool:
    assert result == expected
    return True
