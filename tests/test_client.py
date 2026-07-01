import httpx
import pytest
import respx

from tasave import AsyncTasaVE, TasaVE, TasaVEError

BASE = "https://tasave.sudelca.com"

RATE_PAYLOAD = {
    "bcv_usd": 104.23,
    "bcv_eur": 112.5,
    "parallel_usdt": 108.1,
    "parallel_buy": 107.5,
    "parallel_sell": 108.7,
    "confidence": 92.0,
    "verified": True,
    "checked_against": ["dolarvzla", "binance_p2p"],
    "valid_from": "2026-06-30T00:00:00-04:00",
    "valid_until": "2026-07-01T00:00:00-04:00",
    "next_expected_update": "2026-07-01T16:00:00-04:00",
    "next_business_day": "2026-07-02",
    "is_preliminary": False,
    "official_since": "2026-06-30T14:30:00-04:00",
    "published_at": "2026-06-30T14:30:00-04:00",
    "sources": ["bcv", "dolarvzla"],
    "consensus": True,
    "updated_at": "2026-07-01T09:00:00-04:00",
    "stale": False,
    "stale_since": None,
}


@respx.mock
def test_rates_current_success():
    respx.get(f"{BASE}/v1/rates").mock(return_value=httpx.Response(200, json=RATE_PAYLOAD))
    client = TasaVE()
    rate = client.rates.current()
    assert rate.bcv_usd == 104.23
    assert rate.verified is True


@respx.mock
def test_rates_parallel_requires_key_raises_error():
    respx.get(f"{BASE}/v1/rates/parallel").mock(
        return_value=httpx.Response(401, text="API key required")
    )
    client = TasaVE()
    with pytest.raises(TasaVEError) as exc_info:
        client.rates.parallel()
    assert exc_info.value.status_code == 401


@respx.mock
def test_history_date_not_found():
    respx.get(f"{BASE}/v1/history/2020-01-01").mock(
        return_value=httpx.Response(404, text="No rate found for 2020-01-01")
    )
    client = TasaVE()
    with pytest.raises(TasaVEError) as exc_info:
        client.history.date("2020-01-01")
    assert exc_info.value.status_code == 404


@respx.mock
def test_status_stale_service_unavailable():
    respx.get(f"{BASE}/v1/status").mock(return_value=httpx.Response(503, text="No rate data available"))
    client = TasaVE()
    with pytest.raises(TasaVEError) as exc_info:
        client.status()
    assert exc_info.value.status_code == 503


@respx.mock
@pytest.mark.asyncio
async def test_async_rates_current_success():
    respx.get(f"{BASE}/v1/rates").mock(return_value=httpx.Response(200, json=RATE_PAYLOAD))
    async with AsyncTasaVE() as client:
        rate = await client.rates.current()
        assert rate.bcv_usd == 104.23
