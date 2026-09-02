from typing import Any


def nested_to_py(obj: Any) -> Any:
    if obj.is_integer():
        return obj.get_integer()
    return [nested_to_py(item) for item in obj.get_list()]


def run_mini_parser(solution_class: type, s: str):
    implementation = solution_class()
    return nested_to_py(implementation.deserialize(s))


def assert_mini_parser(result: Any, expected: Any) -> bool:
    assert result == expected
    return True
