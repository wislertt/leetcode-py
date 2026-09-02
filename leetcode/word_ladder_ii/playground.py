# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_ladders, run_find_ladders
from solution import Solution

# %%
# Example test case
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
expected = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]

# %%
result = run_find_ladders(Solution, begin_word, end_word, word_list)
result

# %%
assert_find_ladders(result, expected)
