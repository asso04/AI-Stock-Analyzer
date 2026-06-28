# 📈 AI Stock Analyzer

An AI-powered stock analysis tool built with **Python**, **Phi-3.5 Instruct**, **Hugging Face Transformers**, **yFinance**, and **Plotly**.

The application automatically retrieves financial data for a stock, generates an interactive price chart, and produces a concise financial report using a local Large Language Model (LLM).

---

## Features

* Retrieve real-time stock information using **Yahoo Finance**
* Generate interactive stock price charts with **Plotly**
* Perform AI-powered financial analysis using **Microsoft Phi-3.5 Instruct**
* Run completely locally (no external AI APIs required)
* Structured investment reports
* Easy to extend with additional financial indicators

---

## Technologies

* Python 3.11+
* PyTorch
* Transformers
* BitsAndBytes (4-bit quantization)
* Flash Attention 2
* Plotly
* yFinance

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Stock-Analyzer.git

cd AI-Stock-Analyzer
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Required Libraries

```text
torch
transformers
accelerate
bitsandbytes
flash-attn
plotly
yfinance
```

---

## Download the Model

Download **Microsoft Phi-3.5 Instruct** from Hugging Face and place it inside:

```text
Phi_3.5_instruct/
```

Update the path inside `ai.py` if necessary.

---

## Usage

```python
from main import stock

result = stock("AAPL")

print(result["analysis"])
```

You can replace `"AAPL"` with any supported ticker:

```python
stock("MSFT")
stock("NVDA")
stock("TSLA")
stock("AMZN")
stock("META")
```

---

## AI Prompt

The language model is instructed to generate only structured financial reports.

Output format:

* Overview
* Financial Health
* Strengths
* Weaknesses
* Risks
* Valuation
* Technical Analysis
* Final Decision
* Score (0–10)
* Recommendation (BUY / HOLD / SELL)

The prompt also restricts:

* introductions
* macroeconomic discussions
* generic explanations
* unstructured output

---

## Future Improvements

* Financial ratios dashboard
* Candlestick charts
* Technical indicators (RSI, MACD, Bollinger Bands)
* Earnings reports
* News sentiment analysis
* Portfolio tracking
* Streamlit or Flask web interface
* Multi-stock comparison
* PDF report export
* Historical performance scoring

---

## Disclaimer

The generated analyses do **not** constitute financial advice. Always conduct your own research before making investment decisions.


