# Unscrapable Problems List

# Problems that cannot be scraped due to being premium, API issues, or other
# technical limitations.

# Format: (problem_number, problem_name)

# Already handled (created, or confirmed not applicable).
UNSCRAPABLE_HANDLED = [
    (252, "meeting-rooms"),
    (253, "meeting-rooms-ii"),
    (261, "graph-valid-tree"),
    (271, "encode-and-decode-strings"),
    (285, "inorder-successor-in-bst"),
    (362, "design-hit-counter"),
    (759, "employee-free-time"),
    (286, "walls-and-gates"),
    (323, "number-of-connected-components-in-an-undirected-graph"),
    (437, "path-sum-iii"),
    (1730, "shortest-path-to-get-food"),
    (156, "binary-tree-upside-down"),
    (159, "longest-substring-with-at-most-two-distinct-characters"),
    (161, "one-edit-distance"),
    (163, "missing-ranges"),
    (186, "reverse-words-in-a-string-ii"),
    (243, "shortest-word-distance"),
    (244, "shortest-word-distance-ii"),
    (246, "strobogrammatic-number"),
    (247, "strobogrammatic-number-ii"),
    (248, "strobogrammatic-number-iii"),
    (249, "group-shifted-strings"),
    (250, "count-univalue-subtrees"),
    (251, "flatten-2d-vector"),
    (254, "factor-combinations"),
    (255, "verify-preorder-sequence-in-binary-search-tree"),
    (256, "paint-house"),
    (259, "3sum-smaller"),
    (265, "paint-house-ii"),
    (266, "palindrome-permutation"),
    (267, "palindrome-permutation-ii"),
    (269, "alien-dictionary"),
    (270, "closest-bst-value"),
    (272, "closest-bst-value-ii"),
    (276, "paint-fence"),
    (277, "find-the-celebrity"),
    (280, "wiggle-sort"),
    (281, "zigzag-iterator"),
    (291, "word-pattern-ii"),
    (293, "flip-game"),
    (294, "flip-game-ii"),
    (296, "best-meeting-point"),
    (298, "binary-tree-longest-consecutive-sequence"),
    (302, "smallest-rectangle-enclosing-black-pixels"),
    (305, "number-of-islands-ii"),
    (308, "range-sum-query-2d-mutable"),
    (311, "sparse-matrix-multiplication"),
    (314, "binary-tree-vertical-order-traversal"),
    (317, "shortest-distance-from-all-buildings"),
    (320, "generalized-abbreviation"),
    (325, "maximum-size-subarray-sum-equals-k"),
    (333, "largest-bst-subtree"),
    (339, "nested-list-weight-sum"),
    (340, "longest-substring-with-at-most-k-distinct-characters"),
    (346, "moving-average-from-data-stream"),
    (348, "design-tic-tac-toe"),
    (351, "android-unlock-patterns"),
    (353, "design-snake-game"),
    (356, "line-reflection"),
    (358, "rearrange-string-k-distance-apart"),
    (359, "logger-rate-limiter"),
    (360, "sort-transformed-array"),
    (361, "bomb-enemy"),
    (364, "nested-list-weight-sum-ii"),
    (366, "find-leaves-of-binary-tree"),
    (369, "plus-one-linked-list"),
    (370, "range-addition"),
    (379, "design-phone-directory"),
    (408, "valid-word-abbreviation"),
    (411, "minimum-unique-word-abbreviation"),
    (418, "sentence-screen-fitting"),
    (422, "valid-word-square"),
    (425, "word-squares"),
    (426, "convert-binary-search-tree-to-sorted-doubly-linked-list"),
    (428, "serialize-and-deserialize-n-ary-tree"),
    (431, "encode-n-ary-tree-to-binary-tree"),
    (439, "ternary-expression-parser"),
    (444, "sequence-reconstruction"),
    (465, "optimal-account-balancing"),
    (469, "convex-polygon"),
    (471, "encode-string-with-shortest-length"),
    (484, "find-permutation"),
    (487, "max-consecutive-ones-ii"),
    (489, "robot-room-cleaner"),
    (490, "the-maze"),
    (499, "the-maze-iii"),
    (505, "the-maze-ii"),
    (510, "inorder-successor-in-bst-ii"),
    (527, "word-abbreviation"),
    (531, "lonely-pixel-i"),
    (545, "boundary-of-binary-tree"),
    (548, "split-array-with-equal-sum"),
    (549, "binary-tree-longest-consecutive-sequence-ii"),
    (555, "split-concatenated-strings"),
    (582, "kill-process"),
    (604, "design-compressed-string-iterator"),
    (616, "add-bold-tag-in-string"),
    (625, "minimum-factorization"),
    (631, "design-excel-sum-formula"),
    (634, "find-the-derangement-of-an-array"),
    (635, "design-log-storage"),
    (642, "design-search-autocomplete-system"),
    (644, "maximum-average-subarray-ii"),
    (651, "4-keys-keyboard"),
    (656, "coin-path"),
    (694, "number-of-distinct-islands"),
    (708, "insert-into-a-sorted-circular-linked-list"),
    (711, "number-of-distinct-islands-ii"),
    (716, "max-stack"),
    (723, "candy-crush"),
    (734, "sentence-similarity"),
    (737, "sentence-similarity-ii"),
    (742, "closest-leaf-in-a-binary-tree"),
    (751, "ip-to-cidr"),
    (760, "find-anagram-mappings"),
    (772, "basic-calculator-iii"),
    (774, "minimize-max-distance-to-gas-station"),
    (1055, "shortest-way-to-form-string"),
    (1056, "confusing-number"),
    (1057, "campus-bikes"),
    (1058, "minimize-rounding-error-to-meet-target"),
    (1059, "all-paths-from-source-lead-to-destination"),
    (1060, "missing-element-in-sorted-array"),
    (1086, "high-five"),
    (1087, "brace-expansion"),
    (1088, "confusing-number-ii"),
    (1099, "two-sum-less-than-k"),
    (1100, "find-k-length-substrings-with-no-repeated-characters"),
    (1101, "the-earliest-moment-when-everyone-become-friends"),
    (1102, "path-with-maximum-minimum-value"),
    (1120, "maximum-average-subtree"),
    (1121, "divide-array-into-increasing-sequences"),
    (1133, "largest-unique-number"),
    (1134, "armstrong-number"),
    (1135, "connecting-cities-with-minimum-cost"),
    (1136, "parallel-courses"),
    (1150, "check-if-a-number-is-majority-element-in-a-sorted-array"),
    (1152, "analyze-user-website-visit-pattern"),
    (1165, "single-row-keyboard"),
    (1166, "design-file-system"),
    (1167, "minimum-cost-to-connect-sticks"),
    (1168, "optimize-water-distribution-in-a-village"),
    (1180, "count-substrings-with-only-one-distinct-letter"),
    (1183, "maximum-number-of-ones"),
    (1196, "how-many-apples-can-you-put-into-the-basket"),
    (1198, "find-smallest-common-element-in-all-rows"),
    (1214, "two-sum-bsts"),
    (1215, "stepping-numbers"),
    (1216, "valid-palindrome-iii"),
    (1228, "missing-number-in-arithmetic-progression"),
    (1229, "meeting-scheduler"),
    (1230, "toss-strange-coins"),
    (1231, "divide-chocolate"),
    (1236, "web-crawler"),
    (1243, "array-transformation"),
    (1244, "design-a-leaderboard"),
    (1245, "tree-diameter"),
    (1246, "palindrome-removal"),
    (1258, "synonymous-sentences"),
    (1259, "handshakes-that-dont-cross"),
    (1272, "remove-interval"),
    (1273, "delete-tree-nodes"),
    (1274, "number-of-ships-in-a-rectangle"),
    (1426, "counting-elements"),
    (1427, "perform-string-shifts"),
    (1428, "leftmost-column-with-one"),
    (1429, "first-unique-number"),
    (1474, "delete-n-nodes-after-m-nodes-of-a-linked-list"),
    (1490, "clone-n-ary-tree"),
    (1506, "find-root-of-n-ary-tree"),
    (1522, "diameter-of-n-ary-tree"),
    (1533, "find-the-index-of-the-large-integer"),
]

# Todo queue in discovery order. Move a tuple into UNSCRAPABLE_HANDLED once the
# problem is created; append new discoveries at the bottom.
UNSCRAPABLE_QUEUE = [
    (1197, "minimum-knight-moves"),
    (1538, "guess-the-majority-in-a-hidden-array"),
    (1564, "put-boxes-into-the-warehouse-i"),
    (1570, "dot-product-of-two-sparse-vectors"),
    (1650, "lowest-common-ancestor-of-a-binary-tree-iii"),
    (1762, "buildings-with-an-ocean-view"),
    (1836, "remove-duplicates-from-an-unsorted-linked-list"),
    (1279, "traffic-light-controlled-intersection"),
    (1265, "print-immutable-linked-list-in-reverse"),
]

# Problems that cannot be implemented in Python (SQL, shell, etc.).
# Never created; kept separate from the unscrapable lists so the todo queue
# stays purely actionable.
NON_PYTHON_PROBLEMS = [
    (262, "trips-and-users"),
    (1264, "page-recommendations"),
    (1280, "students-and-examinations"),
    (511, "game-play-analysis-i"),
    (512, "game-play-analysis-ii"),
    (550, "game-play-analysis-iv"),
    (1141, "user-activity-for-the-past-30-days-i"),
    (1142, "user-activity-for-the-past-30-days-ii"),
    (1251, "average-selling-price"),
    (1270, "all-people-report-to-the-given-manager"),
]


def is_unscrapable(problem_number: int) -> bool:
    """Check if a problem number is in the unscrapable list."""
    return any(num == problem_number for num, _ in UNSCRAPABLE_HANDLED + UNSCRAPABLE_QUEUE)


def is_unscrapable_by_name(problem_name: str) -> bool:
    """Check if a problem name is in the unscrapable list."""
    return any(name == problem_name for _, name in UNSCRAPABLE_HANDLED + UNSCRAPABLE_QUEUE)


def get_unscrapable_numbers() -> set[int]:
    """Get all unscrapable problem numbers as a set."""
    return {num for num, _ in UNSCRAPABLE_HANDLED + UNSCRAPABLE_QUEUE}


def get_non_python_numbers() -> set[int]:
    """Get all non-Python (SQL, shell, ...) problem numbers as a set."""
    return {num for num, _ in NON_PYTHON_PROBLEMS}


def get_unscrapable_queue() -> list[tuple[int, str]]:
    """Get the todo queue in discovery order.

    Queue entries that turn out to be already-created are the caller's
    staleness check.
    """
    return list(UNSCRAPABLE_QUEUE)
