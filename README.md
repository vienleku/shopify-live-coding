# Shopify Full-Stack Live Coding

Two-part live coding exercise for the **Shopify Full-Stack Developer** role.

- **Part A — Liquid theme** (15 min): a low-stock badge section in Dawn.
- **Part B — Webhook + dedupe** (30 min): idempotent order ingestion in FastAPI.

The environment is fully pre-configured — no local installs needed. Open this repo
in GitHub Codespaces (green **Code** button → **Codespaces** tab → **Create codespace**),
or click: `https://codespaces.new/vienleku/shopify-live-coding`

First build takes ~2 minutes (`setup.sh` installs Shopify CLI, Python deps, and clones Dawn).

---

## Part A — Liquid theme (15 min)

Using the **Dawn** theme in `theme/`, build a **low-stock badge** on the product page:

1. Show a `Low stock` badge when available inventory is at or below a threshold (default **3**).
2. Make the threshold overridable per-product via a metafield (`custom.low_stock_threshold`); fall back to the default when unset.
3. Build it as a **reusable section** with a proper JSON schema:
   - an enable/disable toggle,
   - a setting for the badge text,
   - a setting for the badge color.
4. Mobile-friendly (Dawn is mobile-first).

To see it live:

```bash
cd theme
shopify theme dev        # one-time `shopify login` first
```

**Rules:** no AI assistants for this part — it's fundamentals.

---

## Part B — Webhook + dedupe (30 min)

A Shopify store fires `orders/create` webhooks at your service. Build an **idempotent**
handler so that a replayed webhook never creates a second shipment.

In `part-b/`, implement the three `TODO`s in `main.py`:

1. Derive the **idempotency key** from the order `id` (Shopify sends it as a number — store/compare it as a string).
2. If the order was already processed, reject as a **duplicate** (`409`) — no courier call, no second row.
3. For a **new** order: insert one row, POST the shipment to the courier, write the status back via `shopify_api.write_order_status()`, return `201`.

**The mock courier** (`mock_courier.py`, port 8001) logs every request to `shipments.log`.
**The Shopify write-back** (`shopify_api.py`) is a stub that logs to `status_writes.log` — in production it'd hit the Admin API.

### Run it (three terminals)

```bash
# terminal 1 — mock courier (port 8001)
python3 mock_courier.py

# terminal 2 — your API (port 8000)
uvicorn main:app --reload --port 8000

# terminal 3 — self-check
bash test.sh
```

`test.sh` POSTs the fixture twice and prints the two status codes, the DB row count, and the courier log count. Correct behaviour: **201 then 409, 1 row, 1 shipment.**

**Rules:** AI assistants and docs are allowed here — it's the real workflow. It reveals whether you *read* docs or just accept output.

---

## What "done" looks like

See `rubric.md` for the exact grading criteria.
