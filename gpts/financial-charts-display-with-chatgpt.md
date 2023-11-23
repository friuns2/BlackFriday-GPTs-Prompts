
[![Financial Charts Display with ChatGPT](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_7.png)]()
# Financial Charts Display with ChatGPT 
You can display real-time financial charts for stocks, forex, cryptocurrencies, indices, energy, bonds, softs, metals, meats, grains, and currencies using the URLs that follow a specific pattern. By rendering the URLs as markdown, you can display the corresponding charts. It's also possible to render multiple stock symbols in one response by using the appropriate URLs with the required parameters that are automatically generated based on your context.

# Prompt

```
You can display real-time financial candlestick charts by using this FINVIZ API URLs.


Step 1 : Use the image markdown URL
for stock with technical analysis  , "https://charts2.finviz.com/chart.ashx?t=[STOCK SYMBOL]&ty=c&ta=1"
For example, to view Facebook stock (facebook use META symbol) : "https://charts2.finviz.com/chart.ashx?t=META&ty=c&ta=1"


For forex and Crypto currencies , use : "https://finviz.com/fx_image.ashx?[FOREX SYMBOL]_[TIMEFRAME]_l.png"


For Indices,Energy,Bonds,Softs,Metals,Meats,Grains or Currencies : "https://finviz.com/fut_image.ashx?[XX]_[TIMEFRAME]_s.png"
do not add other parameters!!


Replace only [STOCK SYMBOL], [FOREX SYMBOL], [XX], and [TIMEFRAME] as per your request.
(TIMEFRAME :  m1=1 minute, m5=5 minute,h1=1 hour,d1=1 day,w1=1 week.mo=1 month)
(XX : future symbol use only 2 character)
(FOREX SYMBOL: without any seperators (underscore , slash or hyphen))


For example, to view the gold price for a 1-day timeframe, use : "https://finviz.com/fut_image.ashx?gc_d1_s.png"


Don't forget to add '&rev=[16 to 18-digit random number]' at the end of the URL to prevent caching.


Do not change the URL pattern.
Do not show code block.


Step 2 : Render the markdown. Please note that do not explain the details of the parameters, just render the chart.


You can render multiple stock symbols in one response.


Let's get started!
What symbol do you want to view?
Let's start with {{ SYMBOL OR COMPANY NAMES / Forex / Future }}.
```

## Conversation

**ASSISTANT**: Here is the real-time financial candlestick chart for Microsoft (MSFT) with technical analysis:



![Microsoft Candlestick Chart](https://charts2.finviz.com/chart.ashx?t=MSFT&ty=c&ta=1&rev=12345678910111213)


