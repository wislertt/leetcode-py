def _abbr_len(abbr: str) -> int:
    return sum(1 for c in abbr if c.isalpha()) + sum(1 for c in abbr if c.isdigit())


def _abbr_matches(abbr: str, word: str) -> bool:
    i = j = 0
    while i < len(abbr) and j < len(word):
        if abbr[i].isdigit():
            if abbr[i] == "0":
                return False
            k = 0
            while i < len(abbr) and abbr[i].isdigit():
                k = k * 10 + int(abbr[i])
                i += 1
            j += k
        else:
            if word[j] != abbr[i]:
                return False
            i += 1
            j += 1
    return i == len(abbr) and j == len(word)


def _min_abbreviation(target: str, dictionary: list[str]) -> str:
    m = len(target)
    words = [w for w in dictionary if len(w) == m]
    best_abbr = None
    best_len = None
    for mask in range(1 << m):
        parts: list[str] = []
        run = 0
        for i, ch in enumerate(target):
            if mask >> i & 1:
                if run:
                    parts.append(str(run))
                    run = 0
                parts.append(ch)
            else:
                run += 1
        if run:
            parts.append(str(run))
        candidate = "".join(parts)
        candidate_len = _abbr_len(candidate)
        if best_len is not None and candidate_len > best_len:
            continue
        if (best_len is None or candidate_len < best_len) and not any(
            _abbr_matches(candidate, w) for w in words
        ):
            best_abbr, best_len = candidate, candidate_len
    return best_abbr or ""


def run_min_abbreviation(solution_class: type, target: str, dictionary: list[str]):
    implementation = solution_class()
    return implementation.min_abbreviation(target, dictionary)


def assert_min_abbreviation(result: str, target: str, dictionary: list[str]) -> bool:
    # result must be a shortest abbreviation of target conflicting with no dictionary word.
    best_abbr = _min_abbreviation(target, dictionary)
    assert _abbr_matches(result, target)
    assert all(not _abbr_matches(result, w) for w in dictionary)
    assert len(result) == len(best_abbr)
    return True
