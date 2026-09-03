import pytest

from leetcode_py import logged_test

from .helpers import assert_subdomain_visits, run_subdomain_visits
from .solution import Solution


class TestSubdomainVisitCount:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "cpdomains, expected",
        [
            (["9001 d.leetcode.com"], ["9001 com", "9001 d.leetcode.com", "9001 leetcode.com"]),
            (["900 g.mail.com"], ["900 com", "900 g.mail.com", "900 mail.com"]),
            (["50 yahoo.com", "5 wiki.org"], ["5 org", "5 wiki.org", "50 com", "50 yahoo.com"]),
            (["9 g.m.com", "1 i.m.com"], ["1 i.m.com", "10 com", "10 m.com", "9 g.m.com"]),
            (["1 a.com"], ["1 a.com", "1 com"]),
            (["10 mail.com"], ["10 com", "10 mail.com"]),
            (["2 zz.com"], ["2 com", "2 zz.com"]),
            (["3 a.b.c"], ["3 a.b.c", "3 b.c", "3 c"]),
            (["2 x.com", "3 x.com"], ["5 com", "5 x.com"]),
            (["1 a.b", "1 b.a"], ["1 a", "1 a.b", "1 b", "1 b.a"]),
            (["10000 site.org"], ["10000 org", "10000 site.org"]),
            (["1 a.b.c", "2 d.e.f"], ["1 a.b.c", "1 b.c", "1 c", "2 d.e.f", "2 e.f", "2 f"]),
            (["9999 x.sub.tld"], ["9999 sub.tld", "9999 tld", "9999 x.sub.tld"]),
            (["7 a.b"], ["7 a.b", "7 b"]),
            (["2 mail.com", "3 mail.org"], ["2 com", "2 mail.com", "3 mail.org", "3 org"]),
            (["1 q.r.s", "1 r.s"], ["1 q.r.s", "2 r.s", "2 s"]),
            (["4 a.com", "6 b.org"], ["4 a.com", "4 com", "6 b.org", "6 org"]),
        ],
    )
    def test_subdomain_visits(self, cpdomains: list[str], expected: list[str]):
        result = run_subdomain_visits(Solution, cpdomains)
        assert_subdomain_visits(result, expected)
