class HtmlParser:
    # Test-harness API: backs the getUrls interface with the url library
    def __init__(self, urls: list[str], edges: list[list[int]]) -> None:
        self.adj: dict[str, list[str]] = {u: [] for u in urls}
        for a, b in edges:
            self.adj[urls[a]].append(urls[b])

    def get_urls(self, url: str) -> list[str]:
        return self.adj[url]


class Solution:
    # Time: O(V + E) pages and links visited once
    # Space: O(V) visited set
    def crawl(self, start_url: str, html_parser: HtmlParser) -> list[str]:
        host = start_url[7:].split("/")[0]
        visited = {start_url}
        stack = [start_url]
        while stack:
            url = stack.pop()
            for link in html_parser.get_urls(url):
                if link in visited or link[7:].split("/")[0] != host:
                    continue
                visited.add(link)
                stack.append(link)
        return list(visited)
