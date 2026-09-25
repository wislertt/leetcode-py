Output lcpy-preview.gif
Set Shell "zsh"
Set FontSize 18
Set Width 960
Set Height 640
Set Theme {"background":"#0E1621","foreground":"#D8DEE9","cursor":"#FFE052","cursor_text":"#0E1621","selection_background":"#387EB8","selection_foreground":"#F2F7FC","palette":["#22303C","#E06C5E","#6FBF73","#FFE052","#6FB3E0","#C88AD2","#62C1D8","#D8DEE9","#3E525F","#EC8B7D","#8FD48A","#FFD43B","#82BCE6","#D8A8E0","#7FD0E4","#EDF2F7"]}
Set Padding 42
Set CursorBlink false

# Hidden warm-up. Hide pauses frame capture, so none of this (including the
# Sleep durations) lands in the GIF. lcpy's cold start is 10-14s; a visible
# cold command outruns any reasonable Sleep and cascades typed commands into
# each other. Running everything once here warms imports and pyc caches so
# every visible command finishes well inside its dwell. venv with pytest +
# leetcode-py-sdk must exist before rendering (see setup.sh).
Hide
Type "source .venv/bin/activate"
Enter
Sleep 2s
Type "lcpy gen -n 1 --force --no-check > /dev/null 2>&1"
Enter
Sleep 40s
Type "pytest --tb=no --no-summary -q > /dev/null 2>&1"
Enter
Sleep 15s
Type "python -c 'from leetcode_py.data_structures import TreeNode' > /dev/null 2>&1"
Enter
Sleep 5s
Type "rm -rf two_sum"
Enter
Sleep 1s
Type "clear"
Enter
Sleep 1s
Show

# beat 1: generate the environment
Type "lcpy gen -n 1 --no-check"
Enter
Sleep 8s
Type "ls two_sum"
Enter
Sleep 2500ms

# beat 2: tests fail first
Hide
Type "clear"
Enter
Sleep 1s
Show
Type "echo '15 test cases, zero code'"
Enter
Sleep 800ms
Type "pytest --tb=no --no-summary -q"
Enter
Sleep 3s

# beat 3: fill in the stub
Hide
Type "clear"
Enter
Sleep 1s
Show
Type "echo 'fill in the stub'"
Enter
Sleep 800ms
Type "cat > two_sum/solution.py <<'EOF'"
Enter
Type "class Solution:"
Enter
Type "    # Time: O(n)"
Enter
Type "    # Space: O(n)"
Enter
Type "    def two_sum(self, nums: list[int], target: int) -> list[int]:"
Enter
Type "        seen = {}"
Enter
Type "        for i, n in enumerate(nums):"
Enter
Type "            if target - n in seen:"
Enter
Type "                return [seen[target - n], i]"
Enter
Type "            seen[n] = i"
Enter
Type "        return []"
Enter
Type "EOF"
Enter
Sleep 1500ms

# beat 4: green
Hide
Type "clear"
Enter
Sleep 1s
Show
Type "pytest --tb=no --no-summary -q"
Enter
Sleep 3s

# beat 5: ascii tree in the terminal
Hide
Type "clear"
Enter
Sleep 1s
Show
Type "echo 'visualize in the terminal, no jupyter'"
Enter
Sleep 800ms
Type "python"
Enter
Sleep 1500ms
Type "from leetcode_py.data_structures import TreeNode"
Enter
Sleep 1200ms
Type "print(TreeNode.from_list([3, 9, 20, None, None, 15, 7]))"
Enter
Sleep 3s
Type "exit()"
Enter
Sleep 800ms
