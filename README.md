# 📈 AI Stock Analyzer

An AI-powered stock analysis tool built with **Python**, **Phi-3.5 Instruct**, **Hugging Face Transformers**, **yFinance**, and **Plotly**.

The system retrieves real-time financial data, generates interactive stock charts, and produces structured investment analysis using a local Large Language Model.

---

## 🚀 Features

* Real-time stock data via **Yahoo Finance**
* AI financial analysis using **Microsoft Phi-3.5 Instruct**
* Interactive price charts with **Plotly**
* Fully local inference (no external AI APIs)
* Structured investment reports
* Easily extendable architecture

---

## 📁 Project Structure

```text
project/
│
├── ai.py              # LLM financial analysis (Phi-3.5 prompt engine)
├── finance.py         # Yahoo Finance data retrieval
├── charts.py          # Plotly chart generation
├── app.py             # Main application entry point
├── requirements.txt   # Project dependencies
│
├── Phi_3.5_instruct/  # Local LLM model directory
│
└── README.md
```

---

## 🧠 How It Works

1. `app.py` is executed as the entry point
2. Stock data is fetched via `finance.py`
3. Historical prices are visualized using `charts.py`
4. Financial metrics are sent to the LLM in `ai.py`
5. The model returns a structured financial report

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Stock-Analyzer.git
cd AI-Stock-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

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

## 🤖 Model Setup

Download **Phi-3.5 Instruct** from Hugging Face and place it in:

```text
Phi_3.5_instruct/
```

Update the path inside `ai.py` if needed.

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

Example usage inside code:

```python
from app import stock

result = stock("AAPL")

print(result["analysis"])
```

Supported tickers:

```text
AAPL, MSFT, NVDA, TSLA, AMZN, META
```

---

## 📈 Output Components

Each analysis includes:

* Company overview
* Financial health
* Strengths & weaknesses
* Risk assessment
* Valuation analysis
* Technical analysis
* Final decision
* Score (0–10)
* BUY / HOLD / SELL recommendation

---

## 🔮 Future Improvements

* Candlestick charts (OHLC)
* Technical indicators (RSI, MACD, Bollinger Bands)
* News sentiment analysis
* Portfolio tracking system
* Web dashboard (Streamlit / FastAPI)
* Multi-stock comparison engine
* PDF report export
* Backtesting module

---

⚡ Hardware Requirements

This system is designed for GPU execution.

- CUDA-enabled GPU required for optimal performance
- 4-bit quantized inference (bitsandbytes)
- Flash Attention 2 support for improved efficiency

CPU execution is supported but not optimized and may result in high latency.

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.

It does not constitute financial advice. Always perform independent analysis before making investment decisions.

---

## 📄 License

This project is proprietary. Commercial use requires explicit permission from the author.
