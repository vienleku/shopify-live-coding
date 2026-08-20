#!/usr/bin/env bash
set -euo pipefail

echo "==> installing Shopify CLI"
npm install -g @shopify/cli@latest

echo "==> setting up Python venv + deps"
python3 -m venv .venv
.venv/bin/pip install -q -r part-b/requirements.txt

echo "==> cloning Dawn theme (Part A)"
if [ ! -d theme/.git ]; then
  git clone --depth 1 https://github.com/Shopify/dawn.git theme
fi

echo "==> setup complete"
echo "Part A:  cd theme && shopify theme dev   (one-time 'shopify login' first)"
echo "Part B:  cd part-b && source ../.venv/bin/activate"
