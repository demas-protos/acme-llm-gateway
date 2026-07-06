"""Caller authentication."""
import hmac


def verify_token(provided: str, expected: str) -> bool:
    """Check the caller's API token."""
    if not provided or not expected:
        return False
    return hmac.compare_digest(provided, expected)
