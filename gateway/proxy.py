"""Upstream proxy."""
import logging

import httpx

log = logging.getLogger(__name__)

MAX_PROMPT_CHARS = 100_000


def forward(prompt, upstream):
    if len(prompt) > MAX_PROMPT_CHARS:
        raise ValueError("prompt too long")
    log.info("forwarding prompt to %s", upstream)
    resp = httpx.post(upstream, json={"prompt": prompt}, timeout=30)
    return resp.json()
