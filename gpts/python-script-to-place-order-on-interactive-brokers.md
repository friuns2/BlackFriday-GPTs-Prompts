
[![Python script to place order on Interactive Brokers ](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_4.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22LxsDBBxxc0NsdykY6-cZ9%22%2C%22flow%22%3Atrue%7D%7D)
# Python script to place order on Interactive Brokers  | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22LxsDBBxxc0NsdykY6-cZ9%22%2C%22flow%22%3Atrue%7D%7D)
Python script to place order on Interactive Brokers by taking the values from trading view indicator

# Prompt

```
write a python program to take a webhook from trading view in this format

{"Action": "Buy", "Ticker": "AAPL", "Price": 370}

and place an order on Interactive Brokers. Take relevant values from the webhook and place the order with 30% of the account balance
```

## Conversation

**ASSISTANT**: Here's an example Python program that uses Flask to receive a webhook from TradingView, and places an order on Interactive Brokers using 30% of the account balance:



```python

from flask import Flask, request

from ibapi.client import EClient

from ibapi.wrapper import EWrapper

from ibapi.contract import Contract

from ibapi.common import *

from ibapi.order import *



class IBAPIClient(EWrapper, EClient):

    def __init__(self):

        EClient.__init__(self, self)

        self.nextOrderId = None



    def nextValidId(self, orderId: int):

        super().nextValidId(orderId)

        self.nextOrderId = orderId



    def placeOrder(self, contract: Contract, order: Order):

        self.placeOrder(self.nextOrderId, contract, order)

        self.nextOrderId += 1



app = Flask(__name__)



@app.route('/webhook', methods=['POST'])

def webhook():

    data = request.json

    action = data['Action']

    ticker = data['Ticker']

    price = float(data['Price'])



    # Connect to IB TWS or Gateway

    client = IBAPIClient()

    client.connect('127.0.0.1', 4002, clientId=0)



    # Get account balance

    account_data = []

    class AccountInfo(EWrapper, EClient):

        def __init__(self):

            EClient.__init__(self,self)

        def error(self, reqId:TickerId, errorCode:int, errorString:str):

            print("Error:",reqId,"Code:",errorCode,"Msg:",errorString)

        def updateAccountValue(self, key:str, val:str, currency:str, accountName:str):

            account_data.append((key,val))

    ai = AccountInfo()

    client.reqAccountSummary(9001, "All", "$LEDGER")

    while len(account_data) == 0:

        client.run()

    account_balance = float(dict(account_data)['TotalCashValue'])



    # Calculate order quantity

    order_quantity = int((account_balance * 0.3) / price)



    # Create contract object for the specified ticker

    contract = Contract()

    contract.symbol = ticker

    contract.secType = 'STK'

    contract.exchange = 'SMART'

    contract.currency = 'USD'



    # Create a limit order

    order_type = 'BUY' if action.upper() == 'BUY' else 'SELL'

    limit_order = LimitOrder(order_type, order_quantity, price)



    try:

        # Place the order

        client.placeOrder(contract, limit_order)

    except Exception as e:

        # Handle any errors that occur during the order placement process

        print(f'Error placing order: {e}')



    # Disconnect from IB TWS or Gateway

    client.disconnect()



    return 'OK'



if __name__ == '__main__':

    app.run()

```



This program receives the webhook request, extracts the `Action`, `Ticker`, and `Price` fields from the JSON payload, creates a contract object for the specified ticker, calculates the order quantity based on 30% of the account balance and the specified price, creates a limit order using the specified action, quantity, and price, and then places the order on Interactive Brokers. Finally, it returns an HTTP response indicating success by returning the string `'OK'`.



Note that you'll need to have an active connection to the IB TWS or Gateway in order to place orders. Additionally, this program doesn't handle any error cases that may occur during the order placement process, so you may want to add additional error handling to make it more robust.
**USER**: Include doc strings in the code
**ASSISTANT**: Here's an updated version of the code that includes docstrings to explain what each class and function does, as well as what inputs they expect and what outputs they produce:



```python

from flask import Flask, request

from ibapi.client import EClient

from ibapi.wrapper import EWrapper

from ibapi.contract import Contract

from ibapi.common import *

from ibapi.order import *



class IBAPIClient(EWrapper, EClient):

    """Class that handles messages from the Interactive Brokers API."""



    def __init__(self):

        """Initialize the class."""

        EClient.__init__(self, self)

        self.nextOrderId = None



    def nextValidId(self, orderId: int):

        """Handler for the 'next valid order ID' message."""

        super().nextValidId(orderId)

        self.nextOrderId = orderId



    def placeOrder(self, contract: Contract, order: Order):

        """Place an order using the Interactive Brokers API."""

        self.placeOrder(self.nextOrderId, contract, order)

        self.nextOrderId += 1



app = Flask(__name__)



@app.route('/webhook', methods=['POST'])

def webhook():

    """

    Handle incoming webhooks from TradingView.



    Expects a JSON payload with the following fields:

    - Action: "BUY" or "SELL"

    - Ticker: The symbol of the security to trade (e.g. "AAPL")

    - Price: The price at which to buy/sell the security

    """



    data = request.json

    action = data['Action']

    ticker = data['Ticker']

    price = float(data['Price'])



    # Connect to IB TWS or Gateway

    client = IBAPIClient()

    client.connect('127.0.0.1', 4002, clientId=0)



    # Get account balance

    account_data = []

    class AccountInfo(EWrapper, EClient):

        def __init__(self):

            EClient.__init__(self,self)

        def error(self, reqId:TickerId, errorCode:int, errorString:str):

            print("Error:",reqId,"Code:",errorCode,"Msg:",errorString)

        def updateAccountValue(self, key:str, val:str, currency:str, accountName:str):

            account_data.append((key,val))

    ai = AccountInfo()

    client.reqAccountSummary(9001, "All", "$LEDGER")

    while len(account_data) == 0:

        client.run()

    account_balance = float(dict(account_data)['TotalCashValue'])



    # Calculate order quantity

    order_quantity = int((account_balance * 0.3) / price)



    # Create contract object for the specified ticker

    contract = Contract()

    contract.symbol = ticker

    contract.secType = 'STK'

    contract.exchange = 'SMART'

    contract.currency = 'USD'



    # Create a limit order

    order_type = 'BUY' if action.upper() == 'BUY' else 'SELL'

    limit_order = LimitOrder(order_type, order_quantity, price)



    try:

        # Place the order

        client.placeOrder(contract, limit_order)

    except Exception as e:

        # Handle any errors that occur during the order placement process

        print(f'Error placing order: {e}')



    # Disconnect from IB TWS or Gateway

    client.disconnect()



    return 'OK'



if __name__ == '__main__':

    app.run()

```



The docstrings explain what each class and function does, as well as what inputs they expect and what outputs they produce. They also provide a description of the expected JSON payload format for incoming TradingView webhooks. Docstrings are an important part of writing clear, maintainable code as they make it easier for other developers (and yourself in the future) to understand what the code does without having to read through every line of code.


