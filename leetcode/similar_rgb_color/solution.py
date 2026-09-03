class Solution:
    # Time: O(1)
    # Space: O(1)
    def similar_rgb(self, color: str) -> str:
        def nearest(channel: str) -> str:
            val = int(channel, 16)
            q = val // 17 + (1 if val % 17 > 8 else 0)
            return f"{17 * q:02x}"

        return "#" + "".join(nearest(color[i : i + 2]) for i in (1, 3, 5))
