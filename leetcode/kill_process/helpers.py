def run_kill_process(solution_class: type, pid: list[int], ppid: list[int], kill: int):
    implementation = solution_class()
    return implementation.kill_process(pid, ppid, kill)


def assert_kill_process(result: list[int], expected: list[int]) -> bool:
    # Order-independent comparison
    assert sorted(result) == sorted(expected)
    return True
