"""Part B starter — idempotent Shopify order webhook ingestion.

Implement the three TODOs below. Expected behaviour is in README.md and
rubric.md; the quick self-check is `bash test.sh` (with both servers running).

Run:
    Terminal 1:  python3 mock_courier.py              (port 8001)
    Terminal 2:  uvicorn main:app --reload --port 8000
    Terminal 3:  bash test.sh
"""
from fastapi import FastAPI, HTTPException, Request

from db import get_db, init_db
from shopify_api import write_order_status

COURIER_URL = "http://127.0.0.1:8001/shipment"

app = FastAPI()
init_db()


@app.post("/webhook/order")
async def order_webhook(request: Request):
    payload = await request.json()

    # TODO 1 — derive the idempotency key from the order id.
    #         (Shopify sends `id` as a number; store/compare it as a string.)
    order_id = None

    # TODO 2 — if this order was already processed, reject it as a duplicate
    #         (HTTP 409) WITHOUT calling the courier or inserting a row again.

    # TODO 3 — for a NEW order: insert one row, POST the shipment to
    #         COURIER_URL, call write_order_status(order_id, status), return 201.
    raise HTTPException(status_code=501, detail="not implemented")
