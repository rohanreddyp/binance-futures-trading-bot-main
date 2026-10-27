from rich import print
from rich.panel import Panel

from bot.validators import (
    validate_side,
    validate_quantity
)

from bot.orders import (
    place_market_order,
    place_limit_order
)

print(
    Panel.fit(
        "PrimeTrade Binance Testnet Bot"
    )
)

print("\n1. Market Order")
print("2. Limit Order")

choice = input(
    "\nSelect Option: "
)

symbol = input(
    "Enter Symbol: "
).upper()

side = validate_side(
    input(
        "BUY / SELL: "
    )
)

quantity = validate_quantity(
    input(
        "Quantity: "
    )
)

if choice == "1":

    print("\nORDER SUMMARY")
    print("-" * 30)

    print("Symbol :", symbol)
    print("Side   :", side)
    print("Type   : MARKET")
    print("Qty    :", quantity)

    confirm = input(
        "\nConfirm Order (Y/N): "
    )

    if confirm.upper() == "Y":

        try:

            result = place_market_order(
                symbol,
                side,
                quantity
            )

            print("\nSUCCESS")
            print("-" * 30)

            print(
                "Order ID:",
                result.get("orderId")
            )

            print(
                "Status:",
                result.get("status")
            )

            print(
                "Executed Qty:",
                result.get("executedQty")
            )

            print(
                "Avg Price:",
                result.get("avgPrice")
            )

        except Exception as e:

            print("\nORDER FAILED")
            print("-" * 30)
            print(e)

    else:

        print("\nOrder Cancelled")

elif choice == "2":

    price = float(
        input(
            "Price: "
        )
    )

    print("\nORDER SUMMARY")
    print("-" * 30)

    print("Symbol :", symbol)
    print("Side   :", side)
    print("Type   : LIMIT")
    print("Qty    :", quantity)
    print("Price  :", price)

    confirm = input(
        "\nConfirm Order (Y/N): "
    )

    if confirm.upper() == "Y":

        try:

            result = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

            print("\nSUCCESS")
            print("-" * 30)

            print(
                "Order ID:",
                result.get("orderId")
            )

            print(
                "Status:",
                result.get("status")
            )

            print(
                "Executed Qty:",
                result.get("executedQty")
            )

            print(
                "Avg Price:",
                result.get("avgPrice")
            )

        except Exception as e:

            print("\nORDER FAILED")
            print("-" * 30)
            print(e)

    else:

        print("\nOrder Cancelled")

else:

    print(
        "\nInvalid Option"
    )