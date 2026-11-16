FREE_SHIPPING_THRESHOLD = 5_000
STANDARD_SHIPPING_FEE = 499


def apply_discount(total_cents: int, discount_pct: int) -> int:
    discount_cents = total_cents * discount_pct // 100
    return total_cents - discount_cents


def subtotal(items: list[tuple[int, int]]) -> int:
    return sum(price_cents * quantity for price_cents, quantity in items)


def shipping_fee(subtotal_cents: int) -> int:
    if subtotal_cents >= FREE_SHIPPING_THRESHOLD:
        return 0
    return STANDARD_SHIPPING_FEE


def checkout(items: list[tuple[int, int]], discount_pct: int) -> int:
    for price_cents, quantity in items:
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
    if not 0 <= discount_pct <= 100:
        raise ValueError("discount_pct must be between 0 and 100")
    total = subtotal(items)
    return apply_discount(total, discount_pct) + shipping_fee(total)


if __name__ == "__main__":
    print(checkout([(2_500, 2)], discount_pct=10))