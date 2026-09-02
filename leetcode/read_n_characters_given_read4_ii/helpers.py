from .solution import File


def run_read(solution_class: type, file: str, queries: list[int]):
    file_api = File(file)
    implementation = solution_class()
    results: list[int] = []
    consumed = 0
    for n in queries:
        buf = [""] * n
        count = implementation.read(buf, n, file_api)
        # each call must fill buf with the next count characters
        assert "".join(buf[:count]) == file[consumed : consumed + count]
        consumed += count
        results.append(count)
    return results


def assert_read(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
