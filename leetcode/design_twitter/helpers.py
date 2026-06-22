from typing import Any


def run_twitter(solution_class: type, operations: list[str], inputs: list[list[int]]):
    twitter: Any = None
    results: list[Any] = []

    for op, args in zip(operations, inputs, strict=False):
        if op == "Twitter":
            twitter = solution_class()
            results.append(None)
        elif op == "postTweet":
            assert twitter is not None
            twitter.post_tweet(args[0], args[1])
            results.append(None)
        elif op == "getNewsFeed":
            assert twitter is not None
            results.append(twitter.get_news_feed(args[0]))
        elif op == "follow":
            assert twitter is not None
            twitter.follow(args[0], args[1])
            results.append(None)
        elif op == "unfollow":
            assert twitter is not None
            twitter.unfollow(args[0], args[1])
            results.append(None)

    return results


def assert_twitter(result: list[Any], expected: list[Any]) -> bool:
    assert result == expected
    return True
