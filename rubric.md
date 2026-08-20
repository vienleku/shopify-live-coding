# Grading Rubric

## Part A — Liquid theme (15 min)

| Criterion | Strong (2) | OK (1) | Weak (0) |
|---|---|---|---|
| **Section structure** | Correct `{% schema %}` + section file, renderable | Works but schema/structure off | No section, hard-coded in template |
| **JSON schema settings** | Toggle + text + color settings, sensible defaults | Settings present but incomplete | No schema settings |
| **Liquid control flow** | Clean `{% if %}` / `for` over variants, no repetition | Works but clunky | Broken logic |
| **Metafield fallback** | Reads `custom.low_stock_threshold` with default fallback | Hard-codes threshold only | Ignores metafield |
| **Mobile / classes** | Uses Dawn tokens/classes, mobile-safe | Functional but not responsive-aware | Breaks mobile layout |

**Signals to watch:** does he use Dawn's existing section conventions, or fight them? Does he test on a mobile viewport? Does he ask about where the badge should sit (product page vs PDP template)?

---

## Part B — Webhook + dedupe (30 min)

| Criterion | Strong (2) | OK (1) | Weak (0) |
|---|---|---|---|
| **Idempotency key** | Correctly derives key from order `id`, normalises to string | Key correct but type-fragile | No real key / uses nothing |
| **Duplicate detection** | Returns 409 without side-effects, uses DB uniqueness | Detects dup but has a race / extra write | No dedupe |
| **New-order path** | Insert + courier POST + status write, returns 201 | Happy path works, minor gaps | Doesn't complete the path |
| **Error handling** | Handles courier failure without crashing/duplicating | Partial handling | Crashes on courier failure |
| **Readability** | Clear, minimal, idempotent-by-construction | Works but convoluted | Spaghetti |

**Signals to watch:**
- Does he state the idempotency key *before* coding, or fumble?
- Does he ask about failure/retry, or only happy-path it?
- Does he talk through trade-offs (unique constraint vs. SELECT-then-INSERT race), or go silent?
- Does he verify his own work with `test.sh`, or claim "done" unverified?
