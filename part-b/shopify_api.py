"""Stub for the "write status back to the order" Shopify Admin API step.

In production this would POST to the Shopify Admin API (orders/{id}.json) or set
a metafield/note. Here it logs the mutation to stdout + status_writes.log so the
interviewer can verify it fired.
"""
import json

LOG = "status_writes.log"


def write_order_status(order_id: str, status: str) -> None:
    entry = {"order_id": order_id, "status": status}
    with open(LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[shopify] write status: {entry}")
