# PrimeTrade Binance Futures Testnet Trading Bot

## Features

* Market Orders
* Limit Orders
* BUY and SELL Support
* Binance Futures Testnet Integration
* CLI Based User Interface
* Input Validation
* Logging
* Error Handling

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a .env file:

API_KEY=your_api_key

API_SECRET=your_secret_key

## Run

```bash
python cli.py
```

## Example

1. Market Order
2. Limit Order

Select Option: 2

Enter Symbol: BTCUSDT

BUY / SELL: BUY

Quantity: 0.001

Price: 50000

## Logs

Logs are stored in:

logs/trading.log

## Project Structure

bot/

* client.py
* orders.py
* validators.py
* logger.py

cli.py
README.md
requirements.txt
