from .solution import MountainArray


class _ListMountainArray(MountainArray):
    def __init__(self, arr: list[int]) -> None:
        self._arr = arr
        self.calls = 0

    def get(self, index: int) -> int:
        self.calls += 1
        if self.calls > 100:
            raise RuntimeError("Exceeded 100 MountainArray.get() calls")
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


def run_find_in_mountain_array(solution_class: type, arr: list[int], target: int):
    mountain_arr = _ListMountainArray(arr)
    implementation = solution_class()
    return implementation.find_in_mountain_array(target, mountain_arr)


def assert_find_in_mountain_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
