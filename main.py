import tkinter as tk
from utils.binance_API import BinanceAPI     
from components.ticker import PriceCard,BidAskCard,VolumeCard
from components.orderbook import OrderBook
from components.chart import Chart
from utils import config                     

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BTCUSDT Dashboard")
        self.root.geometry("1000x600")
        self.root.configure(bg=config.BACKGROUND_COLOR)
        self.setup_ui()
        self.api = BinanceAPI(self.handle_data)
        self.api.start()

    def setup_ui(self):
        control_frame = tk.Frame(self.root, bg=config.COMPONENT_BG)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(control_frame, text="Select Asset:", bg=config.COMPONENT_BG, fg="white", font=config.FONT_MAIN).pack(side="left", padx=10)
        
        assets = ["BTCUSDT", "ETHUSDT", "SOLUSDT","DOGEUSDT", "SHIBUSDT"]
        for asset in assets:
            btn = tk.Button(control_frame, text=asset, 
                            command=lambda a=asset: self.change_coin(a),
                            bg="gray", fg="black")
            btn.pack(side="left", padx=5, pady=5)
        top_frame = tk.Frame(self.root, bg=config.BACKGROUND_COLOR)
        top_frame.pack(fill="x", padx=10, pady=10)

        self.price_card = PriceCard(top_frame, "Last Traded Price")
        self.price_card.pack(side="left", fill="both", expand=True, padx=5)

        self.bid_ask_card = BidAskCard(top_frame)
        self.bid_ask_card.pack(side="left", fill="both", expand=True, padx=5)
        
        self.volume_card = VolumeCard(top_frame, "24h Statistics")
        self.volume_card.pack(side="left", fill="both", expand=True, padx=5)
        
        bottom_frame = tk.Frame(self.root, bg=config.BACKGROUND_COLOR)
        bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.chart_frame = tk.Frame(bottom_frame, bg="black", width=600)
        self.chart_frame.pack(side="right", fill="both", expand=True, padx=5)
        
        bottom_frame = tk.Frame(self.root, bg=config.BACKGROUND_COLOR)
        bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.order_book = OrderBook(bottom_frame)
        self.order_book.pack(side="left", fill="both", expand=True, padx=5)

        self.chart = Chart(bottom_frame)
        self.chart.pack(side="right", fill="both", expand=True, padx=5)
        
    def change_coin(self, new_symbol):
        print(f"Switching to {new_symbol}...")
        self.current_coin = new_symbol
        self.price_card.title_label.config(text=f"{new_symbol} Price")
        self.chart.times = []
        self.chart.opens = []
        self.chart.highs = []
        self.chart.lows = []
        self.chart.closes = []
        self.chart.ax.clear()
        self.chart.ax.set_title(f"{new_symbol} 1 Minute Chart", color='white')
        self.chart.canvas.draw()
        self.api.start(new_symbol)
        
    def handle_data(self, data):
        stream = response.get('stream')
        data = response.get('data')

        if not data: return

        if 'ticker' in stream:
            price = data['c']
            change = data['p']
            bid = data['b']
            ask = data['a']
            vol_btc = data['v']
            vol_usdt = data['q']
            self.root.after(0, self.update_ticker_ui, 
                            data['c'], data['p'], data['P'], data['b'], data['a'], data['v'], data['q'])
        
        elif 'depth' in stream:
            bids = data['bids']
            asks = data['asks']
            self.root.after(0, self.order_book.update_data, bids, asks)

        elif 'kline' in stream: 
            k = data['k']
            self.root.after(0, self.chart.update_candle, k['t'], float(k['o']), float(k['h']), float(k['l']), float(k['c']))
    def update_ticker_ui(self, price, change, bid, ask, vol_btc, vol_usdt):
        self.price_card.update_data(price, change)
        self.bid_ask_card.update_data(bid, ask)
        self.volume_card.update_data(vol_btc, vol_usdt)
        
    def on_closing(self):
        self.api.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()