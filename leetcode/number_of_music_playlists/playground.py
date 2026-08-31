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
from helpers import assert_num_music_playlists, run_num_music_playlists
from solution import Solution

# %%
# Example test case
n = 3
goal = 3
k = 1
expected = 6

# %%
result = run_num_music_playlists(Solution, n, goal, k)
result

# %%
assert_num_music_playlists(result, expected)
