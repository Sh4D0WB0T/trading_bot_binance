import argparse
from bot.client import BinanceClient
from bot.validators import *
from bot.orders import log_order_request, log_order_response, log_error

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    client = BinanceClient()

    try:
        # ✅ VALIDATION
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        # ✅ PARAMS
        params = {
            "symbol": args.symbol,
            "side": args.side,
            "type": args.type,
            "quantity": args.quantity
        }

        if args.type == "LIMIT":
            params["price"] = args.price
            params["timeInForce"] = "GTC"

        # ✅ LOG REQUEST
        log_order_request(params)

        print("\n📌 ORDER REQUEST")
        print(params)

        # ✅ PLACE ORDER
        response = client.place_order(**params)

        # ✅ LOG RESPONSE
        log_order_response(response)

        print("\n✅ ORDER SUCCESS")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except ValueError as ve:
        log_error(ve)
        print(f"\n{ve}")

    except Exception as e:
        log_error(e)
        print("\n❌ ORDER FAILED")
        print(str(e))

if __name__ == "__main__":
    main()