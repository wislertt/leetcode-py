from .solution import File


def run_read(solution_class: type, file: str, n: int):
    file_api = File(file)
    buf = [""] * n
    count = solution_class().read(buf, n, file_api)
    # read must fill buf with the first count characters of the file
    assert "".join(buf[:count]) == file[:count]
    return count


def assert_read(result: int, expected: int) -> bool:
    assert result == expected
    return True
