def calculate_payment_fee(amount: float) -> float:
    if amount <= 0:
        raise ValueError("Payment amount must be positive")

    return round(amount * 0.02, 2)


def get_payment_status(transaction_id: str) -> str:
    if not transaction_id:
        raise ValueError("Transaction ID is required")

    return "SUCCESS"


if __name__ == "__main__":
    transaction_id = "TXN1001"
    amount = 5000.00

    fee = calculate_payment_fee(amount)
    status = get_payment_status(transaction_id)

    print(f"Transaction ID: {transaction_id}")
    print(f"Payment Amount: {amount}")
    print(f"Payment Fee: {fee}")
    print(f"Payment Status Updated: {status}")