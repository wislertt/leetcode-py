class Solution:
    # Time: O(1) - at most 16 button-parity vectors, each scored on <= 3 bulbs
    # Space: O(1) - at most 8 distinct statuses
    def flip_lights(self, n: int, presses: int) -> int:
        # Bulb j flips iff: button 1 (always), button 2 (j even),
        # button 3 (j odd), button 4 (j % 3 == 1). Every bulb's fate is a fixed
        # XOR of these four parities, so for n >= 3 the first three bulbs
        # determine the whole room: two different parity vectors agreeing on
        # bulbs 1-3 also agree on b1^b3 and b4, hence differ on b1 and b3,
        # which every bulb sees. So counting distinct 3-bulb prefixes counts
        # distinct full configurations.
        bulbs = min(n, 3)
        statuses: set[tuple[bool, ...]] = set()
        for mask in range(16):
            used = mask.bit_count()
            if used > presses or (presses - used) % 2 != 0:
                continue
            statuses.add(
                tuple(
                    (
                        (mask & 1)
                        ^ ((mask >> 1) & 1 if bulb % 2 == 0 else 0)
                        ^ ((mask >> 2) & 1 if bulb % 2 == 1 else 0)
                        ^ ((mask >> 3) & 1 if bulb % 3 == 1 else 0)
                    )
                    == 0
                    for bulb in range(1, bulbs + 1)
                )
            )
        return len(statuses)
