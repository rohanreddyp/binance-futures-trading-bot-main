from bot.client import client
from bot.logger import logger
from binance.exceptions import BinanceAPIException


def place_market_order(
        symbol,
        side,
        quantity):

    try:

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(
            f"MARKET ORDER: {response}"
        )

        return response

    except BinanceAPIException as e:

        logger.error(
            f"Binance API Error: {e}"
        )

        raise

    except Exception as e:

        logger.error(
            f"Unexpected Error: {e}"
        )

        raise


def place_limit_order(
        symbol,
        side,
        quantity,
        price):

    try:

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(
            f"LIMIT ORDER: {response}"
        )

        return response

    except BinanceAPIException as e:

        logger.error(
            f"Binance API Error: {e}"
        )

        raise

    except Exception as e:

        logger.error(
            f"Unexpected Error: {e}"
        )

        raise