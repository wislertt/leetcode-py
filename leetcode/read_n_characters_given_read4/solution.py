class File:
    # Test-harness API: backs the read4 interface with the file content
    def __init__(self, content: str) -> None:
        self.content = content
        self.pos = 0

    def read4(self, buf4: list[str]) -> int:
        # Reads up to 4 consecutive characters into buf4 and returns the
        # number of characters actually read
        chunk = self.content[self.pos : self.pos + 4]
        self.pos += len(chunk)
        for i, char in enumerate(chunk):
            buf4[i] = char
        return len(chunk)


class Solution:
    # Time: O(n)
    # Space: O(1)
    def read(self, buf: list[str], n: int, file: File) -> int:
        i = 0
        buf4 = [""] * 4
        while i < n:
            count = file.read4(buf4)
            if count == 0:
                break
            for j in range(min(count, n - i)):
                buf[i] = buf4[j]
                i += 1
        return i
