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
from helpers import (
    assert_find_all_concatenated_words_in_a_dict,
    run_find_all_concatenated_words_in_a_dict,
)
from solution import Solution

# %%
# Example test case
words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
expected = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

# %%
result = run_find_all_concatenated_words_in_a_dict(Solution, words)
result

# %%
assert_find_all_concatenated_words_in_a_dict(result, expected)
