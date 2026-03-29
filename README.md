# Simplified Trading Bot (Binance Futures Testnet)

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- Input validation
- Logging system

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create .env file:
   API_KEY="jitQCgbE4zlotaXQGNN4zZtktp9fu1SRts9g3xtErkdyimEkCBdxVclaRLWJhCYF"
   API_SECRET="LrbUEH3Cr0ER1Q9izYB7qYa9JQrCUs6HvzyfMFcVhcWJdqoj91oiDeeCVJF5vCxV"
   BASE_URL=https://testnet.binancefuture.com

## Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000

## Logs
Stored in logs/trading_bot.log
