def run_magic_dictionary(solution_class: type, operations: list[str], inputs: list[list[str]]):
    magic = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "MagicDictionary":
            magic = solution_class()
            results.append(None)
        elif op == "build_dict" and magic is not None:
            magic.build_dict(inputs[i][0])
            results.append(None)
        elif op == "search" and magic is not None:
            results.append(magic.search(inputs[i][0]))
    return results, magic


def assert_magic_dictionary(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
