class Codec:
    # Time: O(1) average per operation
    # Space: O(n) for n encoded URLs
    def __init__(self) -> None:
        self.url_map: dict[str, str] = {}
        self.encode_map: dict[str, str] = {}

    def encode(self, long_url: str) -> str:
        if long_url in self.encode_map:
            return self.encode_map[long_url]
        short_url = f"http://tinyurl.com/{len(self.url_map)}"
        self.url_map[short_url] = long_url
        self.encode_map[long_url] = short_url
        return short_url

    def decode(self, short_url: str) -> str:
        return self.url_map[short_url]
