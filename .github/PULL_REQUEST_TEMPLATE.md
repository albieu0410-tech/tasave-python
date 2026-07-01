## What does this PR do?

<!-- Describe the change and why it's needed. -->

## Related issue

<!-- Link the issue this addresses, if any. -->

## Checklist

- [ ] Follows the existing client shape (`client.rates.current()`,
      `client.history.range(...)`, etc.) — no parallel API surface
- [ ] Added or updated tests in `tests/test_client.py`
- [ ] `uv run pytest -v` passes
- [ ] Model changes match the shape served by `tasave-api`
