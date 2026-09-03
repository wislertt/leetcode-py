class Solution:
    # Time: O(log n)
    # Space: O(log n)
    def find_integers(self, n: int) -> int:
        bits = bin(n)[2:]
        fib = [1, 2]
        while len(fib) < len(bits):
            fib.append(fib[-1] + fib[-2])

        count = 0
        prev_bit = 0
        for i, bit_char in enumerate(bits):
            if bit_char == "1":
                count += fib[len(bits) - i - 1]
                if prev_bit == 1:
                    count -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
        return count + 1
