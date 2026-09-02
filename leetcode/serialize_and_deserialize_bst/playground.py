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
from helpers import assert_round_trip, run_serialize_deserialize
from solution import Codec

# %%
# Example test case
root_list = [2, 1, 3]

# %%
result = run_serialize_deserialize(Codec, root_list)
result

# %%
assert_round_trip(result, root_list)
