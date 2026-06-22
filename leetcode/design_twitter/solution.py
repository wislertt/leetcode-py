import heapq


class Twitter:
    def __init__(self) -> None:
        self.tweets: dict[int, list[tuple[int, int]]] = {}
        self.following: dict[int, set[int]] = {}
        self.timestamp = 0

    # Time: O(1)
    # Space: O(1)
    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.timestamp += 1
        self.tweets.setdefault(user_id, []).append((self.timestamp, tweet_id))

    # Time: O(F * T log(F * T)) where F = followee count, T = tweets per user (bounded by 10)
    # Space: O(F * 10)
    def get_news_feed(self, user_id: int) -> list[int]:
        followees = self.following.get(user_id, set()) | {user_id}
        heap: list[tuple[int, int]] = []
        for followee in followees:
            # Only the 10 most recent per user can ever appear in the top-10 feed
            for time, tweet_id in self.tweets.get(followee, [])[-10:]:
                heapq.heappush(heap, (time, tweet_id))
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(reverse=True)
        return [tweet_id for _, tweet_id in heap]

    # Time: O(1)
    # Space: O(1)
    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id == followee_id:
            return
        self.following.setdefault(follower_id, set()).add(followee_id)

    # Time: O(1)
    # Space: O(1)
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.following.get(follower_id, set()).discard(followee_id)
