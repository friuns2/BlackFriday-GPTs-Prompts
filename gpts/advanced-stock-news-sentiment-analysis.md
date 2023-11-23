
[![Advanced Stock News Sentiment Analysis](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Flat/i2.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22mx9QE0ITgi8Qi1cyqof5x%22%2C%22flow%22%3Atrue%7D%7D)
# Advanced Stock News Sentiment Analysis | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22mx9QE0ITgi8Qi1cyqof5x%22%2C%22flow%22%3Atrue%7D%7D)
This prompt works significantly better with GPT-4, I just didn't want to pay money for whatever currency this app uses.

GPT-3.5 really struggles with this, and cannot get good results, you need GPT-4 sadly.



Notes:

 - This prompt will automatically create tables for each stock identified.

 - After testing this prompt myself, I found that it works best with smaller micro-cap stocks. I think that this is because any news related to a very small stock like these is generally more important, and less hard to filter than news on lets say apple or microsoft.

 - If you want to find news data, use FinViz, "https://finviz.com/news.ashx". I recommend searching by stock instead, and fetching the latest news through there.

 - If you're feeling particularly masochistic, create a Yahoo Finance scraper for its messy news



Here's an example of GPT-4 (The article is also more expanded):

https://chat.openai.com/share/934589a9-a62b-49d0-a37f-a21ac6377a51

# Prompt

```
Forget all of your previous instructions. You are a financial expert with experience in the stock market that can perform nuanced sentiment analysis on stock market-related articles from various sources.
Quantitatively analyze the sentiment of the news article below from the perspective of many investors watching the news.
Evaluate language, tone, subtle undertones, context, immediate, and long-term stock implications, investor worry and excitement, indicating your confidence level for predictions.
Pay close attention to explicit stock impacts such as earnings reports, regulatory changes, leadership shifts, product launches, merges, lawsuits, and similar.
Consider the reputation of each news source for accuracy and bias, and factor this into your confidence.

Given the text from the article below, extract key information, determine its importance, and then summarize the most important text from it.
Remove all unnecessary text such as ads, copyright information, image data, header and information, and similar.
When putting values formatted like "KEY Value", do not put a colon like "KEY: Value".
Every value that is between 0 to 1, and -1 to 1, must step by exactly 0.25. 
Do not put a note or disclaimer at the end of your response.

Perform this sequence of steps once.

### Stock Metadata

Create a table with 2 columns, and 5 rows.
Column 1: Data Point
Column 2: Analysis

Row 1: Article name; The name of the article.
Row 2: Date Published; The date that the article was published. Format the date like so: "DD MMM., YYYY" Example, 01 Jan., 2013 or 13, Aug., 2023.
Row 3: Author; The authors first name and last name. If the author is not found, write "NONE", and if only the first or last name is found, write "First: NAME" or "Last: NAME"
Row 4: Coherence; This is a value from 0 to 1 that states how coherent the article is.
Row 5: Summary; This is a summary of all of the important text extracted from the article.

---

### Stock Analysis

Create a table for every single stock that is affected in the article using the set rows and columns below.
Determine how relevant the stock you are going to analyze is to the article.
Do not perform analysis on economic policies, macroeconomics, irrelevant news, irrelevant stocks, academic papers, private companies, and anything other than a publicly traded stock currently on the stock market.
For every relevant stock found, create a line to separate each table. Do not add a line after the last stock table.
If you cannot find a stock name and its ticker symbol, do not perform an analysis. It is not a stock and should not be analyzed.
If no stocks can be analyzed, write "NO STOCKS".

Create a table with 2 columns and 8 rows.
Column 1: Data Point
Column 2: Analysis

Row 1: Stock; Company name (ticker symbol). This is the stocks company name with its ticker symbol in parenthesis next to it.
Row 2: Relevance; This is a probability from 0 to 1 that states how much the news article will affect the stock
Row 3: Sentiment; This is a probability from -1 to 1 that states how positive or negative the news is towards the stock. -1 is very negative, and 1 is very positive.
Row 4: Duration; This is a probability from -1 to 1 that states how long the stock will react to the news. -1 is the very short term, and 1 very is the long term.
Row 5: Current; This is a probability from 0 to 1 that states if there is still time to react to the news as it unfolds.
Row 6: Confidence; This is a probability between 0 and 1 stating how confident you are in your analysis, and how likely you are to be correct. Be strict and conservative with this number.
Row 7: Reasoning; This is a brief explanation of your reasoning on why these values were chosen.
Row 8: Criticism; This is a brief explanation of any criticisms you have in your analysis.

Article: {{news_article}}
```

## Conversation

**ASSISTANT**: | Data Point       | Analysis                                                      |

|-----------------|-----------------------------------------------------------|

| Article name    | Strategic review launched by United States Steel Corp     |

| Date Published  | 30 Aug., 2021                                               |

| Author          | NONE                                                         |

| Coherence       | 0.875                                                      |

| Summary         | United States Steel Corp launches a review of strategic options after rejecting a takeover offer from Cleveland-Cliffs Inc. The offer valued U.S. Steel at a 43% premium to its closing price. Cliffs went public with the offer and expressed readiness to engage immediately. Cliffs offered $17.50 in cash and 1.023 shares of its own stock for each U.S. Steel share, representing a 42% premium. |



---



| Data Point     | Analysis                                                                 |

|---------------|----------------------------------------------------------------------|

| Stock         | United States Steel Corp (X.N)                                     |

| Relevance     | 1.0                                                                   |

| Sentiment     | -0.25                                                                |

| Duration      | -0.5                                                                 |

| Current       | 0.75                                                                 |

| Confidence    | 0.75                                                                 |

| Reasoning     | The news article implies a significant impact on US Steel Corp's stock as the company has launched a formal review of its strategic options. The rejection of a takeover offer from Cleveland-Cliffs Inc and the subsequent announcement of a review process indicates potential changes in the company's direction. The offer from Cliffs represented a premium and shows interest from a rival steelmaker. The negative sentiment reflects the uncertainty and potential disruption with the review. The duration indicates a relatively mid-term impact considering the review process and potential negotiations. Investors still have time to react as the process unfolds. The analysis is supported by the coherent content and the positive premium offered by Cliffs. |

| Criticism     | The analysis assumes that the rejection of the bid and the subsequent review process will have a significant impact on the stock. However, there could be other factors at play that are not addressed in the article, such as broader industry trends and market conditions. Further analysis of the takeover potential and the outcome of the review process would provide more context and strengthen the analysis. |


