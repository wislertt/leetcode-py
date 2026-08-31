from bisect import bisect_left


class Solution:
    def suggested_products(self, products: list[str], search_word: str) -> list[list[str]]:
        products = sorted(products)
        result: list[list[str]] = []
        prefix = ""
        for ch in search_word:
            prefix += ch
            start = bisect_left(products, prefix)
            matches = []
            for product in products[start : start + 3]:
                if not product.startswith(prefix):
                    break
                matches.append(product)
            result.append(matches)
        return result
