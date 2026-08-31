import re
from collections import Counter


def run_frequency_sort(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.frequency_sort(s)


def assert_frequency_sort(result: str, expected: str) -> bool:
    assert len(result) == len(expected)
    runs = [m.group() for m in re.finditer(r"(.)\1*", result)]
    freqs = [len(run) for run in runs]
    assert freqs == sorted(freqs, reverse=True)
    assert Counter(result) == Counter(expected)
    return True
