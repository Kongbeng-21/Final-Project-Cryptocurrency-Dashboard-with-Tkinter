# Real-Time Cryptocurrency Dashboard 

A desktop dashboard for tracking cryptocurrency market data in real-time using Python, Tkinter, and Binance WebSocket API.

## Dashboard Preview
### 1. Full Dashboard View
![Main View](cryptodashboard1.png)

### 2. SidePanel Hidden (Chart Focus)
![Hide Panel Mode](cryptodashboard3.png)

### 3. Multi-Asset Support
![Other Coin](cryptodashboard2.png)

## Features
* *Real-Time Data:* Live streaming prices, 24h statistics, and volume via Binance WebSocket.
* *Multi-Asset Support:* Track 5+ cryptocurrencies (BTC, ETH, SOL, DOGE, SHIB).
* *Interactive Charts:* Live 1-minute Candlestick chart built with Matplotlib.
* *Deep Market Data:* Real-time Order Book (Depth 10) and Recent Trades feed.
* *Smart UI:* Dark mode design with color-coded indicators (Green/Red) for price movements.
* *Customizable:* Toggle buttons to hide/show panels and persistent settings (remembers your last view).

## Technologies Used
* *Language:* Python 3.x
* *GUI:* Tkinter
* *Networking:* websocket-client, requests
* *Data Visualization:* Matplotlib
* *Data Handling:* JSON, Threading

## Installation & Usage

1.  *Clone the repository*
    
    git clone <YOUR_GITHUB_LINK_HERE>
    cd crypto_dashboard
    

2.  *Install dependencies*
    
    pip install -r requirements.txt
    

3.  *Run the application*
    
    python main.py
    

## Project Structure
```text
crypto_dashboard/
├── components/          # UI Components (OOP Classes)
│   ├── chart.py         # Candlestick Chart
│   ├── orderbook.py     # Order Book Panel
│   ├── ticker.py        # Price & Stats Cards
│   └── trades.py        # Recent Trades Panel
├── utils/               # Backend Utilities
│   ├── binance_api.py   # WebSocket Connection Manager
│   └── config.py        # Settings & Constants
├── main.py              # Application Entry Point
├── requirements.txt     # Python Dependencies
└── README.md            # Project Documentation