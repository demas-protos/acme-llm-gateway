"""Upstream proxy."""
import httpx


def forward(prompt, upstream):
    resp = httpx.post(upstream, json={"prompt": prompt}, timeout=30)
    return resp.json()
