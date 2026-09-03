class Solution:
    # Time: O(n^2) where n is the length of the sentence (appending index-sized 'a' runs)
    # Space: O(n^2) for the output sentence
    def to_goat_latin(self, sentence: str) -> str:
        vowels = frozenset("aeiouAEIOU")
        words = sentence.split(" ")
        converted = []
        for i, word in enumerate(words, start=1):
            stem = word if word[0] in vowels else word[1:] + word[0]
            converted.append(f"{stem}ma{'a' * i}")
        return " ".join(converted)
