def run_file_system(solution_class: type, operations: list[str], inputs: list[list]):
    from typing import Any

    fs: Any = None
    results: list[bool | int | None] = []
    for i, operation in enumerate(operations):
        if operation == "FileSystem":
            fs = solution_class()
            results.append(None)
        elif operation == "createPath" and fs is not None:
            results.append(fs.create_path(inputs[i][0], inputs[i][1]))
        elif operation == "get" and fs is not None:
            results.append(fs.get(inputs[i][0]))
    return results, fs


def assert_file_system(result: list[bool | int | None], expected: list[bool | int | None]) -> bool:
    assert result == expected
    return True
