class Solution:
    # Time: O(n)
    # Space: O(n)
    def asteroid_collision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                collision = stack[-1] + asteroid
                if collision < 0:
                    stack.pop()
                elif collision > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        return stack
