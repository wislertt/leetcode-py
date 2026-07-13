import heapq


def _build_max_happy(a: int, b: int, c: int) -> str:
    # Reference greedy: always place the most abundant legal char.
    # Produces a max-length happy string (length is deterministic).
    heap: list[tuple[int, str]] = []
    for ch, count in (("a", a), ("b", b), ("c", c)):
        if count > 0:
            heapq.heappush(heap, (-count, ch))
    res: list[str] = []
    while heap:
        neg_cnt, ch = heapq.heappop(heap)
        if len(res) >= 2 and res[-1] == res[-2] == ch:
            if not heap:
                break
            neg2, ch2 = heapq.heappop(heap)
            res.append(ch2)
            if neg2 + 1 < 0:
                heapq.heappush(heap, (neg2 + 1, ch2))
            heapq.heappush(heap, (neg_cnt, ch))
        else:
            res.append(ch)
            if neg_cnt + 1 < 0:
                heapq.heappush(heap, (neg_cnt + 1, ch))
    return "".join(res)


def run_longest_happy_string(solution_class: type, a: int, b: int, c: int):
    implementation = solution_class()
    return implementation.longest_happy_string(a, b, c)


def assert_longest_happy_string(result: str, a: int, b: int, c: int) -> bool:
    # Any valid answer is accepted; verify happiness + maximality.
    assert set(result) <= {"a", "b", "c"}
    assert "aaa" not in result and "bbb" not in result and "ccc" not in result
    assert result.count("a") <= a
    assert result.count("b") <= b
    assert result.count("c") <= c
    assert len(result) == len(_build_max_happy(a, b, c))
    return True
