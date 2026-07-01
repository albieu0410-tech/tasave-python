# Contributing to tasave-python

Thanks for considering a contribution — this SDK is MIT licensed and
community input is welcome.

## Before you start
- For anything non-trivial, open an issue first to discuss the approach
  before writing code.
- The response shapes here must match the `Rate`/`BcvRate`/`ParallelRate`/
  `ConvertResult`/`HistoryEntry`/`Status` models served by the
  [tasave-api](https://github.com/albieu0410-tech/tasaVE) server — check
  that repo's `CLAUDE.md` before changing a model.

## Development setup
```bash
uv sync --extra dev
uv run pytest -v
```

## Pull requests
- Keep PRs focused — one logical change per PR.
- Match the existing client shape: `client.rates.current()`,
  `client.history.range(...)`, etc. Don't introduce a parallel API surface.
- Add or update tests in `tests/test_client.py` for any behavior change.
- Describe *why*, not just *what*, in the PR description.

## Code of conduct
Be respectful. Keep contributions focused on making the SDK a reliable,
faithful client for the TasaVE API.
