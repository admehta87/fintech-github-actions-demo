import pytest

from app import calculate_payment_fee, get_payment_status


def test_calculate_payment_fee():
    assert calculate_payment_fee(5000) == 100.00


def test_calculate_payment_fee_with_decimal():
    assert calculate_payment_fee(1250) == 25.00


def test_calculate_payment_fee_rejects_zero():
    with pytest.raises(ValueError):
        calculate_payment_fee(0)


def test_get_payment_status():
    assert get_payment_status("TXN1001") == "SUCCESS"


def test_get_payment_status_rejects_empty_transaction_id():
    with pytest.raises(ValueError):
        get_payment_status("")

def test_calculate_payment_fee_with_wrong_expectation():
    assert calculate_payment_fee(1000) == 25.00        