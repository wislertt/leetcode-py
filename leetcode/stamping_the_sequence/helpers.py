def _is_valid_stamp_moves(moves: list[int], stamp: str, target: str) -> bool:
    if not 0 <= len(moves) <= 10 * len(target):
        return False
    span = len(target) - len(stamp)
    chars = ["?"] * len(target)
    for move in moves:
        if not 0 <= move <= span:
            return False
        for offset, char in enumerate(stamp):
            chars[move + offset] = char
    return "".join(chars) == target


def run_moves_to_stamp(solution_class: type, stamp: str, target: str):
    implementation = solution_class()
    return implementation.moves_to_stamp(stamp, target)


def assert_moves_to_stamp(result: list[int], expected: list[int], stamp: str, target: str) -> bool:
    # Multiple stamp sequences are valid; an empty one is not reproducible.
    if not expected:
        assert result == []
        return True
    assert result
    assert _is_valid_stamp_moves(result, stamp, target)
    assert len(result) <= 10 * len(target)
    return True
