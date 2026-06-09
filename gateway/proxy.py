"""Upstream proxy."""
import logging

import httpx

log = logging.getLogger(__name__)


def forward(prompt, upstream):
    log.info("forwarding prompt to %s", upstream)
    resp = httpx.post(upstream, json={"prompt": prompt}, timeout=30)
    return resp.json()
