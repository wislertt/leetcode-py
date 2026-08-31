import re
from collections import Counter


class Solution:
    # Time: O(n^2) in the worst case (nested groups merged up the stack)
    # Space: O(n)
    def count_of_atoms(self, formula: str) -> str:
        stack: list[Counter[str]] = [Counter()]
        i, n = 0, len(formula)
        while i < n:
            ch = formula[i]
            if ch == "(":
                stack.append(Counter())
                i += 1
            elif ch == ")":
                i += 1
                mult_match = re.match(r"\d+", formula[i:])
                if mult_match:
                    multiplier = int(mult_match.group())
                    i += len(mult_match.group())
                else:
                    multiplier = 1
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                atom_match = re.match(r"([A-Z][a-z]*)(\d*)", formula[i:])
                if atom_match is None:
                    break
                atom = atom_match.group(1)
                count = int(atom_match.group(2)) if atom_match.group(2) else 1
                i += len(atom_match.group(0))
                stack[-1][atom] += count
        return "".join(
            atom + (str(count) if count > 1 else "") for atom, count in sorted(stack[0].items())
        )
