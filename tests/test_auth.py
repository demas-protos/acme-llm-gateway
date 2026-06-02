from gateway.auth import verify_token


def test_token_ok():
    assert verify_token("abc", "abc")
