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
AI-Stock-Analyzer/
│
├── project/
│   ├── ai.py               
│   ├── app.py         
│   ├── charts.py           
│   ├── finance.py              
│   │
│   └── Phi_3.5_instruct/  
│
├── README.md        
├── license.txt             
├── requirements.txt                
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
git clone https://github.com/asso04/AI-Stock-Analyzer.git
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
pandas
numpy
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
python -m project.app
```

Example usage inside code:

```python
from project.app import stock

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

The LLM may continue generating or truncate its output, and it may be replaced by a more performant model.

It does not constitute financial advice. Always perform independent analysis before making investment decisions.

---

## 📄 License

Commercial use requires explicit permission from the author.
