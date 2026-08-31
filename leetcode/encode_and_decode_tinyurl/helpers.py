def run_encode_and_decode_tinyurl(
    solution_class: type, operations: list[str], inputs: list[list[str]]
):
    codec = None
    results: list[str | None] = []
    last_short: str | None = None
    for op, args in zip(operations, inputs, strict=True):
        if op == "Codec":
            codec = solution_class()
            results.append(None)
        elif op == "encode" and codec is not None:
            last_short = codec.encode(args[0])
            results.append(None)
        elif op == "decode" and codec is not None:
            results.append(codec.decode(last_short or ""))
    return results, codec


def assert_encode_and_decode_tinyurl(result: list[str | None], expected: list[str | None]) -> bool:
    assert result == expected
    return True
