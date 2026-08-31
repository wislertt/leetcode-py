from typing import Any


def run_flatten_nested_list_iterator(solution_class: type, nested_list: list[Any]):
    iterator = solution_class(nested_list)
    results: list[Any] = []
    while iterator.has_next():
        results.append(iterator.next())

    return results


def assert_flatten_nested_list_iterator(result: list[Any], expected: list[Any]) -> bool:
    assert result == expected
    return True
