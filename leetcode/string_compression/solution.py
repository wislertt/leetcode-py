class Solution:
    # Time: O(n)
    # Space: O(1)
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        while read < n:
            ch = chars[read]
            run_start = read
            while read < n and chars[read] == ch:
                read += 1
            run_length = read - run_start
            chars[write] = ch
            write += 1
            if run_length > 1:
                for digit in str(run_length):
                    chars[write] = digit
                    write += 1
        return write
