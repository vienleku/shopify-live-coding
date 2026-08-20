#!/usr/bin/env bash
set -euo pipefail

BASE="http://127.0.0.1:8000"
DB="orders.db"
COURIER_LOG="shipments.log"
STATUS_LOG="status_writes.log"

echo "== resetting state =="
rm -f "$DB" "$COURIER_LOG" "$STATUS_LOG"

echo "== first POST  (expect 201) =="
FIRST=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE/webhook/order" \
  -H "Content-Type: application/json" --data-binary @order_payload.json)
echo "$FIRST"

echo "== second POST (expect 409) =="
SECOND=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE/webhook/order" \
  -H "Content-Type: application/json" --data-binary @order_payload.json)
echo "$SECOND"

echo "== rows in orders.db (expect 1) =="
python3 -c "import sqlite3; print(sqlite3.connect('$DB').execute('select count(*) from orders').fetchone()[0])"

echo "== courier shipments (expect 1) =="
wc -l < "$COURIER_LOG" 2>/dev/null || echo 0

echo "== status writes (expect >=1) =="
wc -l < "$STATUS_LOG" 2>/dev/null || echo 0

echo
if [ "$FIRST" = "201" ] && [ "$SECOND" = "409" ]; then
  echo "PASS: idempotent behaviour correct"
else
  echo "FAIL: got $FIRST / $SECOND (expected 201 / 409)"
  exit 1
fi
