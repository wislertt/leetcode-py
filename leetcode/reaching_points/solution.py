class Solution:
    # Time: O(log(max(tx, ty)))
    # Space: O(1)
    def reaching_points(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Walk backwards from the target: the parent of (x, y) is unique, so
        # collapse runs of same-axis moves with a modulo instead of subtracting.
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        if tx == sx and ty > sy:
            return (ty - sy) % tx == 0
        if ty == sy and tx > sx:
            return (tx - sx) % ty == 0
        return False
