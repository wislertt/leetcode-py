class Solution:
    # Time: O(n)
    # Space: O(n)
    def kill_process(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        children: dict[int, list[int]] = {}
        for child, parent in zip(pid, ppid, strict=True):
            children.setdefault(parent, []).append(child)
        killed: list[int] = []
        stack = [kill]
        while stack:
            cur = stack.pop()
            killed.append(cur)
            stack.extend(children.get(cur, []))
        return killed
