class Solution:
    # Time: O(a + b)
    # Space: O(a + b)
    def str_without3a3b(self, a: int, b: int) -> str:
        result: list[str] = []
        while a > 0 or b > 0:
            # Two identical letters in a row: the other letter is forced.
            # Otherwise extend with the letter that is still more plentiful
            forced = len(result) >= 2 and result[-1] == result[-2]
            write_a = result[-1] == "b" if forced else a >= b
            if write_a:
                result.append("a")
                a -= 1
            else:
                result.append("b")
                b -= 1
        return "".join(result)
