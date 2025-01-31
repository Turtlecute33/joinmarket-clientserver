import jmbitcoin as btc
import pytest
from decimal import Decimal


def test_btc_to_sat() -> None:
    assert(btc.btc_to_sat(Decimal("0.00000001")) == 1)
    assert(btc.btc_to_sat(Decimal("1.00000000")) == 100000000)


def test_sat_to_btc() -> None:
    assert(btc.sat_to_btc(1) == Decimal("0.00000001"))
    assert(btc.sat_to_btc(100000000) == Decimal("1.00000000"))


def test_amount_to_sat() -> None:
    assert(btc.amount_to_sat("1") == 1)
    assert(btc.amount_to_sat("1sat") == 1)
    assert(btc.amount_to_sat("1.123sat") == 1)
    assert(btc.amount_to_sat("0.00000001") == 1)
    assert(btc.amount_to_sat("0.00000001btc") == 1)
    assert(btc.amount_to_sat("0.00000001BTC") == 1)
    assert(btc.amount_to_sat("1.00000000") == 100000000)
    assert(btc.amount_to_sat("1.12300000sat") == 1)
    assert(btc.amount_to_sat("1btc") == 100000000)
    assert(btc.amount_to_sat("1BTC") == 100000000)
    with pytest.raises(ValueError):
        btc.amount_to_sat("")
        btc.amount_to_sat("invalidamount")
        btc.amount_to_sat("123inv")


def test_amount_to_btc() -> None:
    assert(btc.amount_to_btc("1") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("1sat") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("1.123sat") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("0.00000001") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("0.00000001btc") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("0.00000001BTC") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("1.00000000") == 1)
    assert(btc.amount_to_btc("1.12300000sat") == Decimal("0.00000001"))
    assert(btc.amount_to_btc("1btc") == 1)
    assert(btc.amount_to_btc("1BTC") == 1)
    with pytest.raises(ValueError):
        btc.amount_to_btc("")
        btc.amount_to_btc("invalidamount")
        btc.amount_to_btc("123inv")


def test_amount_to_sat_str() -> None:
    assert(btc.amount_to_sat_str("1") == "1 sat")
    assert(btc.amount_to_sat_str("1sat") == "1 sat")
    assert(btc.amount_to_sat_str("1.123sat") == "1 sat")
    assert(btc.amount_to_sat_str("0.00000001") == "1 sat")
    assert(btc.amount_to_sat_str("0.00000001btc") == "1 sat")
    assert(btc.amount_to_sat_str("0.00000001BTC") == "1 sat")
    assert(btc.amount_to_sat_str("1.00000000") == "100000000 sat")
    assert(btc.amount_to_sat_str("1.12300000sat") == "1 sat")
    assert(btc.amount_to_sat_str("1btc") == "100000000 sat")
    assert(btc.amount_to_sat_str("1BTC") == "100000000 sat")
    with pytest.raises(ValueError):
        btc.amount_to_sat_str("")
        btc.amount_to_sat_str("invalidamount")
        btc.amount_to_sat_str("123inv")


def test_amount_to_btc_str() -> None:
    assert(btc.amount_to_btc_str("1") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("1sat") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("1.123sat") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("0.00000001") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("0.00000001btc") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("0.00000001BTC") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("1.00000000") == "1.00000000 BTC")
    assert(btc.amount_to_btc_str("1.12300000sat") == "0.00000001 BTC")
    assert(btc.amount_to_btc_str("1btc") == "1.00000000 BTC")
    assert(btc.amount_to_btc_str("1BTC") == "1.00000000 BTC")
    with pytest.raises(ValueError):
        btc.amount_to_btc_str("")
        btc.amount_to_btc_str("invalidamount")
        btc.amount_to_btc_str("123inv")


def test_amount_to_str() -> None:
    assert(btc.amount_to_str("1") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("1sat") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("1.123sat") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("0.00000001") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("0.00000001btc") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("0.00000001BTC") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("1.00000000") == "1.00000000 BTC (100000000 sat)")
    assert(btc.amount_to_str("1.12300000sat") == "0.00000001 BTC (1 sat)")
    assert(btc.amount_to_str("1btc") == "1.00000000 BTC (100000000 sat)")
    assert(btc.amount_to_str("1BTC") == "1.00000000 BTC (100000000 sat)")
    with pytest.raises(ValueError):
        btc.amount_to_str("")
        btc.amount_to_str("invalidamount")
        btc.amount_to_str("123inv")


def test_sat_to_str() -> None:
    assert(btc.sat_to_str(1) == "0.00000001")
    assert(btc.sat_to_str(100000000) == "1.00000000")


def test_sat_to_str_p() -> None:
    assert(btc.sat_to_str_p(1) == "+0.00000001")
    assert(btc.sat_to_str_p(-1) == "-0.00000001")
    assert(btc.sat_to_str_p(100000000) == "+1.00000000")
    assert(btc.sat_to_str_p(-100000000) == "-1.00000000")


def test_fee_per_kb_to_str() -> None:
    assert(btc.fee_per_kb_to_str(1000) == "1000 sat/kvB (1.0 sat/vB)")
    assert(btc.fee_per_kb_to_str(1234) == "1234 sat/kvB (1.2 sat/vB)")
    assert(btc.fee_per_kb_to_str(1999) == "1999 sat/kvB (1.9 sat/vB)")
