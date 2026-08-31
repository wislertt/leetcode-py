class Solution:
    # Time: O(n)
    # Space: O(n)
    def validate_stack_sequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack: list[int] = []
        pop_index = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return pop_index == len(popped)
