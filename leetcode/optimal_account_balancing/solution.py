class Solution:
    # Time: O(k! ) worst case over k non-zero balances
    # Space: O(k)
    def min_transfers(self, transactions: list[list[int]]) -> int:
        balances: dict[int, int] = {}
        for sender, receiver, amount in transactions:
            balances[sender] = balances.get(sender, 0) - amount
            balances[receiver] = balances.get(receiver, 0) + amount
        debts = [v for v in balances.values() if v != 0]

        def settle(start: int) -> int:
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            best = len(debts)
            seen: set[int] = set()
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0 and debts[i] not in seen:
                    seen.add(debts[i])
                    debts[i] += debts[start]
                    best = min(best, 1 + settle(start + 1))
                    debts[i] -= debts[start]
            return best

        return settle(0)
