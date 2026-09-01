from .solution import HtmlParser


def run_crawl(solution_class: type, urls: list[str], edges: list[list[int]], start_url: str):
    parser = HtmlParser(urls, edges)
    return solution_class().crawl(start_url, parser)


def assert_crawl(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == expected
    return True
