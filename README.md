# tasave

Python client for [TasaVE](https://tasave.sudelca.com) — Venezuelan dollar
exchange rate data (BCV official rate + parallel/P2P rates), multi-source
with confidence scoring.

## Install

```bash
uv add tasave-python
```

## Usage

```python
from tasave import TasaVE

client = TasaVE()  # no API key needed for public endpoints
rate = client.rates.current()

print(rate.bcv_usd)       # 104.23
print(rate.confidence)    # 92.0
print(rate.verified)      # True
```

With an API key (needed for `rates.parallel()` and `history`):

```python
client = TasaVE(api_key="tv_live_...")
parallel = client.rates.parallel()
history = client.history.date("2026-06-30")
```

Async client, same shape:

```python
from tasave import AsyncTasaVE

async with AsyncTasaVE() as client:
    rate = await client.rates.current()
```

## Other endpoints

```python
client.rates.bcv()                                   # BCV official only
client.convert(amount=100, from_currency="USD", to="VES")
client.history.range("2026-06-01", "2026-06-30")
client.status()
```

## Errors

All request failures raise `TasaVEError`, which carries the HTTP status code:

```python
from tasave import TasaVEError

try:
    client.rates.parallel()
except TasaVEError as e:
    print(e.status_code, e.message)  # e.g. 401, "API key required"
```

## License

MIT
