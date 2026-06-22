from . import (
    algo_master_75,
    blind_75,
    grind,
    neetcode_150,
    neetcode_250,
)

available_lists = {
    neetcode_150.tag_name: neetcode_150.problems_list,
    algo_master_75.tag_name: algo_master_75.problems_list,
    blind_75.tag_name: blind_75.problem_list,
    grind.tag_name: grind.problems_list,
    neetcode_250.tag_name: neetcode_250.problems_list,
}
