

# MQL5 Code Generator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22kUUGQ3lb8lybiSqDdYUug%22%2C%22flow%22%3Atrue%7D%7D)
Creates MQL5 Expert Advisor based on the given strategy.

# Prompt

```
I am seeking assistance in generating code for an Expert Advisor (EA) in the MQL5 language, which is to be used in the MetaTrader 5 platform. This code should be developed based on a specific trading strategy that I will provide.

The final deliverable should be the MQL5 code itself, without any additional files or documentation. While writing the code, please make sure to refer to the official MQL5 documentation to ensure accuracy and adherence to best practices.

The code should utilize the ‘Trade.mqh’ library for executing trading orders. This is a crucial aspect of the task as ‘Trade.mqh’ provides a simplified interface for order management.

Lastly, it’s important to note that the code must be written specifically in MQL5. Please do not use MQL4 or any other programming language as they are not compatible with my current requirements.
```

## Welcome Message
Hi, please provide your trading strategy. Include entry, exit rules. Also mention stoploss limit and take profit limit in points. 

## Conversation

**ASSISTANT**: Hi, please provide your trading strategy. Include entry, exit rules. Also mention stoploss limit and take profit limit in points. 
**USER**: Create a expert advisor based on moving average crossover of 20 and 25 EMA. Stop loss 250 points and take profit 400 points.
**ASSISTANT**: Sure! I will create an Expert Advisor based on the moving average crossover strategy you provided. Here's the code:



```mql5

#include <Trade\Trade.mqh>



// Input parameters

input int emaFastPeriod = 20;      // Period of the fast EMA

input int emaSlowPeriod = 25;      // Period of the slow EMA

input int stopLoss = 250;          // Stop loss in points

input int takeProfit = 400;        // Take profit in points



// Global variables

CTrade trade;



// Initialization function

int OnInit()

{

    // Print the EA name and version

    Print("Moving Average Crossover EA v1.0");



    // Set up the trade parameters

    trade.SetExpertMagicNumber(123456); // Change this to a unique number for each instance of the EA



    return(INIT_SUCCEEDED);

}



// Deinitialization function

void OnDeinit(const int reason)

{

    // Print the reason for deinitialization

    Print("Moving Average Crossover EA deinitialized, reason:", reason);

}



// Tick event handler

void OnTick()

{

    // Calculate the fast and slow EMA values

    double emaFast = iMA(Symbol(), 0, emaFastPeriod, 0, MODE_EMA, PRICE_CLOSE, 0);

    double emaSlow = iMA(Symbol(), 0, emaSlowPeriod, 0, MODE_EMA, PRICE_CLOSE, 0);



    // Get the current positions

    int positions = trade.PositionsTotal();



    // Check for a new long position

    if (positions == 0 && emaFast > emaSlow)

    {

        trade.Buy(Symbol(), 0.1, 0, 0, stopLoss, takeProfit);

    }

    // Check for a new short position

    else if (positions == 0 && emaFast < emaSlow)

    {

        trade.Sell(Symbol(), 0.1, 0, 0, stopLoss, takeProfit);

    }

    // Check for open positions

    else if (positions > 0)

    {

        // Check for a long position to close

        if (trade.PositionGetInteger(POSITION_TYPE) == POSITION_TYPE_BUY && emaFast < emaSlow)

        {

            trade.PositionClose(Symbol());

        }

        // Check for a short position to close

        else if (trade.PositionGetInteger(POSITION_TYPE) == POSITION_TYPE_SELL && emaFast > emaSlow)

        {

            trade.PositionClose(Symbol());

        }

    }

}



// The main entry point of the EA

void OnStart()

{

    // Run the tick event handler on every tick

    EventSetTimer(1);

}



//+------------------------------------------------------------------+

```



Please note that this code assumes that you have already installed the `Trade.mqh` library in your MetaTrader 5 platform.



To use this Expert Advisor, save the code as a .mq5 file and compile it in MetaEditor. Then, attach the EA to a chart in MetaTrader 5 and it will start executing trades based on the moving average crossover strategy you provided.



Let me know if you have any questions or if there is anything else I can help you with!

