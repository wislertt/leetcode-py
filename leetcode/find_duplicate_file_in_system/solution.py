from collections import defaultdict


class Solution:
    # Time: O(total characters across all paths)
    # Space: O(total characters) for the content-to-paths map
    def find_duplicate(self, paths: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = defaultdict(list)
        for info in paths:
            dir_path, _, files = info.partition(" ")
            for token in files.split(" "):
                name, content = token[:-1].split("(", 1)
                groups[content].append(f"{dir_path}/{name}")
        return [group for group in groups.values() if len(group) > 1]
