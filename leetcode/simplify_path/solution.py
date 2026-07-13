class Solution:
    # Time: O(n)
    # Space: O(n)
    def simplify_path(self, path: str) -> str:
        stack: list[str] = []

        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)
