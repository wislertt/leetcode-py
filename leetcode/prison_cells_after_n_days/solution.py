class Solution:
    # Time: O(1), at most 256 distinct states so the seen-map cycle search is bounded
    # Space: O(1), the seen map holds at most 256 states
    def prison_after_n_days(self, cells: list[int], n: int) -> list[int]:
        def advance(state: tuple[int, ...]) -> tuple[int, ...]:
            return tuple(int(0 < i < 7 and state[i - 1] == state[i + 1]) for i in range(8))

        state = tuple(cells)
        seen: dict[tuple[int, ...], int] = {}
        for day in range(1, n + 1):
            state = advance(state)
            if state in seen:
                cycle = day - seen[state]
                for _ in range((n - day) % cycle):
                    state = advance(state)
                return list(state)
            seen[state] = day
        return list(state)
