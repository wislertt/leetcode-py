class Solution:
    # Time: O(n) over the total number of characters
    # Space: O(n) for the output lines
    def remove_comments(self, source: list[str]) -> list[str]:
        result: list[str] = []
        in_block = False
        buf: list[str] = []

        for line in source:
            if not in_block:
                buf = []
            i = 0
            while i < len(line):
                if in_block:
                    end = line.find("*/", i)
                    if end == -1:
                        break
                    in_block = False
                    i = end + 2
                else:
                    line_c = line.find("//", i)
                    block_c = line.find("/*", i)
                    if line_c == -1 and block_c == -1:
                        buf.append(line[i:])
                        break
                    if line_c != -1 and (block_c == -1 or line_c < block_c):
                        buf.append(line[i:line_c])
                        break
                    buf.append(line[i:block_c])
                    in_block = True
                    i = block_c + 2
            if not in_block:
                code = "".join(buf)
                if code:
                    result.append(code)

        return result
