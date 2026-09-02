class File:
    # Test-harness API: backs the read4 interface with the file content
    def __init__(self, content: str) -> None:
        self.content = content
        self.pos = 0

    def read4(self, buf4: list[str]) -> int:
        # Reads up to 4 consecutive characters into buf4 and returns the
        # number of characters actually read; read4 keeps its own file
        # pointer across calls
        chunk = self.content[self.pos : self.pos + 4]
        self.pos += len(chunk)
        for i, char in enumerate(chunk):
            buf4[i] = char
        return len(chunk)


class Solution:
    # Time: O(n) per read call
    # Space: O(1), the internal 4-character buffer is reused across calls
    def __init__(self) -> None:
        self.buf4: list[str] = [""] * 4
        self.i = 0  # next unread position inside buf4
        self.size = 0  # number of valid characters currently in buf4

    def read(self, buf: list[str], n: int, file: File) -> int:
        count = 0
        while count < n:
            if self.i == self.size:
                self.size = file.read4(self.buf4)
                self.i = 0
                if self.size == 0:
                    break
            while count < n and self.i < self.size:
                buf[count] = self.buf4[self.i]
                self.i += 1
                count += 1
        return count
