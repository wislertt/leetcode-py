class Solution:
    # Time: O(n) single pass over the input
    # Space: O(d) stack of path lengths, d = max nesting depth
    def length_longest_path(self, input_str: str) -> int:
        best = 0
        # path_lens[i] = total length of the path ending at depth i (dirs only)
        path_lens: list[int] = []
        for line in input_str.split("\n"):
            depth = line.count("\t")
            name = line[depth:]
            del path_lens[depth:]
            parent = path_lens[-1] if path_lens else 0
            length = parent + (1 if path_lens else 0) + len(name)
            if "." in name:
                best = max(best, length)
            else:
                path_lens.append(length)
        return best
