def assert_read_binary_watch_count(result: list[str], turned_on: int, expected_count: int) -> bool:
    assert len(result) == expected_count
    assert len(set(result)) == len(result)
    for time in result:
        hour_str, minute_str = time.split(":")
        hour = int(hour_str)
        minute = int(minute_str)
        assert hour_str == str(hour)
        assert len(minute_str) == 2
        assert 0 <= hour <= 11
        assert 0 <= minute <= 59
        assert hour.bit_count() + minute.bit_count() == turned_on
    return True


def run_read_binary_watch(solution_class: type, turned_on: int):
    implementation = solution_class()
    return implementation.read_binary_watch(turned_on)


def assert_read_binary_watch(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
