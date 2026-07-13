class Solution:
    # Time: O(n)
    # Space: O(1)
    def lemonade_change(self, bills: list[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:  # bill == 20, prefer giving a $10 + $5 to conserve $5 bills
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
