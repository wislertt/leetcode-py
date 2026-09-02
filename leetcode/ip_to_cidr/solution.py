class Solution:
    # Time: O(n) for the range length
    # Space: O(1) excluding the output
    def ip_to_cidr(self, ip: str, n: int) -> list[str]:
        def int_to_ip(x: int) -> str:
            return f"{(x >> 24) & 255}.{(x >> 16) & 255}.{(x >> 8) & 255}.{x & 255}"

        a, b, c, d = (int(part) for part in ip.split("."))
        start = (a << 24) | (b << 16) | (c << 8) | d
        ans: list[str] = []
        while n > 0:
            low = start & -start
            max_block = low if start else 1 << 32
            block = 1
            while block * 2 <= max_block and block * 2 <= n:
                block *= 2
            ans.append(f"{int_to_ip(start)}/{32 - block.bit_length() + 1}")
            start += block
            n -= block
        return ans
