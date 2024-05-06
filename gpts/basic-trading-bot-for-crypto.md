

# Basic Trading Bot for crypto  | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22IYHrckSVrojyiqxvEEqON%22%2C%22flow%22%3Atrue%7D%7D)
Trading strategy that buys when price is above the Simple Moving Average (SMA) and sells when its below the SMA 

# Prompt

```
Code a phemex bot using ccxt and python that trades bitcoin. Buy when price is over the SMA and sell when under.  Just show me the code no explanations needed
```

## Welcome Message
Sure, here is a simple example of a bot that you requested. 



```python

import ccxt

import pandas as pd

import time



# Setup

exchange = ccxt.phemex({

    'apiKey': 'YOUR_API_KEY',

    'secret': 'YOUR_SECRET',

})



markets = exchange.load_markets()

symbol = 'BTC/USD'

market = exchange.market(symbol)



# Calculate SMA

def calculate_sma(data, window):

    if len(data) > window:

        return sum(data[-window:]) / window

    else:

        return None



# Trading bot

def bot():

    balance = exchange.fetch_balance()

    print('Balance:', balance)

    

    data = []

    while True:

        # Fetch latest price

        orderbook = exchange.fetch_order_book(symbol)

        price = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None

        data.append(price)

        

        # Calculate SMA

        sma = calculate_sma(data, 14)

        print('SMA:', sma)

        

        # Check if we should buy or sell

        if price > sma:

            # Buy

            if balance['free']['USD'] > 0:

                print('Buy at:', price)

                exchange.create_market_buy_order(symbol, balance['free']['USD'])

        elif price < sma:

            # Sell

            if balance['free']['BTC'] > 0:

                print('Sell at:', price)

                exchange.create_market_sell_order(symbol, balance['free']['BTC'])

        

        time.sleep(60)



# Run bot

bot()

```



This bot will run indefinitely until stopped. Please remember to replace `'YOUR_API_KEY'` and `'YOUR_SECRET'` with your actual API keys. Also, the bot does not include any error handling or edge case considerations, and you can add them as per your requirements.

## Conversation

**ASSISTANT**: Sure, here is a simple example of a bot that you requested. 



```python

import ccxt

import pandas as pd

import time



# Setup

exchange = ccxt.phemex({

    'apiKey': 'YOUR_API_KEY',

    'secret': 'YOUR_SECRET',

})



markets = exchange.load_markets()

symbol = 'BTC/USD'

market = exchange.market(symbol)



# Calculate SMA

def calculate_sma(data, window):

    if len(data) > window:

        return sum(data[-window:]) / window

    else:

        return None



# Trading bot

def bot():

    balance = exchange.fetch_balance()

    print('Balance:', balance)

    

    data = []

    while True:

        # Fetch latest price

        orderbook = exchange.fetch_order_book(symbol)

        price = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None

        data.append(price)

        

        # Calculate SMA

        sma = calculate_sma(data, 14)

        print('SMA:', sma)

        

        # Check if we should buy or sell

        if price > sma:

            # Buy

            if balance['free']['USD'] > 0:

                print('Buy at:', price)

                exchange.create_market_buy_order(symbol, balance['free']['USD'])

        elif price < sma:

            # Sell

            if balance['free']['BTC'] > 0:

                print('Sell at:', price)

                exchange.create_market_sell_order(symbol, balance['free']['BTC'])

        

        time.sleep(60)



# Run bot

bot()

```



This bot will run indefinitely until stopped. Please remember to replace `'YOUR_API_KEY'` and `'YOUR_SECRET'` with your actual API keys. Also, the bot does not include any error handling or edge case considerations, and you can add them as per your requirements.

