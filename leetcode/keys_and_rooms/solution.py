class Solution:
    # Time: O(n + k) where k is the total number of keys
    # Space: O(n)
    def can_visit_all_rooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        return len(visited) == len(rooms)
