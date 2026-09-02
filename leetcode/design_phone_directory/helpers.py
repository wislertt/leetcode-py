def run_phone_directory(solution_class: type, operations: list[str], inputs: list[list[int]]):
    directory = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "PhoneDirectory":
            directory = solution_class(inputs[i][0])
            results.append(None)
        elif op == "get" and directory is not None:
            results.append(directory.get())
        elif op == "check" and directory is not None:
            results.append(directory.check(inputs[i][0]))
        elif op == "release" and directory is not None:
            directory.release(inputs[i][0])
            results.append(None)
    return results, directory


def assert_phone_directory(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
