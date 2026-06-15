# acme-llm-gateway
A tiny LLM gateway: authenticates callers and proxies prompts upstream.

## Setup
    pip install -r requirements.txt
    export ACME_API_TOKEN=...
    python -m gateway

## Configuration
Set `ACME_UPSTREAM` to the upstream completion endpoint.
