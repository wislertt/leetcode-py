def run_num_music_playlists(solution_class: type, n: int, goal: int, k: int):
    implementation = solution_class()
    return implementation.num_music_playlists(n, goal, k)


def assert_num_music_playlists(result: int, expected: int) -> bool:
    assert result == expected
    return True
