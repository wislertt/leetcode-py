class Solution:
    # Time: O(n)
    # Space: O(n)
    def calculate(self, s: str) -> int:
        def dfs(i: int) -> tuple[int, int]:
            stk: list[int] = []
            num = 0
            sign = "+"
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == "(":
                    num, i = dfs(i + 1)
                if c in "+-*/)" or i == len(s) - 1:
                    if sign == "+":
                        stk.append(num)
                    elif sign == "-":
                        stk.append(-num)
                    elif sign == "*":
                        stk.append(stk.pop() * num)
                    else:
                        stk.append(int(stk.pop() / num))
                    num = 0
                    sign = c
                if c == ")":
                    return sum(stk), i
                i += 1
            return sum(stk), i

        return dfs(0)[0]
