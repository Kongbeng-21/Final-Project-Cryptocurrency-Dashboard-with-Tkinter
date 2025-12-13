import tkinter as tk
from utils import config

class PriceCard(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg=config.COMPONENT_BG)
        self.price_label = tk.Label(self, text="Loading...", bg=config.COMPONENT_BG, fg=config.TEXT_COLOR, font=config.FONT_LARGE)
        self.price_label.pack()

    def update_data(self, price, change,percent):
        color = config.GREEN_COLOR if float(change) >= 0 else config.RED_COLOR
        self.price_label.config(text=f"${float(price):,.2f}\n{float(change):+.2f} ({float(percent):+.2f}%)", fg=color)
class BidAskCard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=config.COMPONENT_BG)
        title = tk.Label(self, text="Best Bid / Ask & Spread", 
                         bg=config.COMPONENT_BG, fg=config.TEXT_COLOR, font=config.FONT_MAIN)
        title.pack(pady=5)
        self.content_frame = tk.Frame(self, bg=config.COMPONENT_BG)
        self.content_frame.pack(expand=True)
        
        self.bid_label = tk.Label(self.content_frame, text="Bid: --", 
                                  bg=config.COMPONENT_BG, fg=config.GREEN_COLOR, font=config.FONT_MAIN)
        self.bid_label.pack(anchor="w")
        
        self.ask_label = tk.Label(self.content_frame, text="Ask: --", 
                                  bg=config.COMPONENT_BG, fg=config.RED_COLOR, font=config.FONT_MAIN)
        self.ask_label.pack(anchor="w")
        
        self.spread_label = tk.Label(self.content_frame, text="Spread: --", 
                                     bg=config.COMPONENT_BG, fg="orange", font=config.FONT_MAIN)
        self.spread_label.pack(anchor="w")

    def update_data(self, bid, ask):
        bid_float = float(bid)
        ask_float = float(ask)
        spread = ask_float - bid_float
        
        self.bid_label.config(text=f"BID(Buy): {bid_float:,.2f}")
        self.ask_label.config(text=f"ASK(Sell): {ask_float:,.2f}")
        self.spread_label.config(text=f"Spread: {spread:.4f}")

class VolumeCard(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg=config.COMPONENT_BG)
        tk.Label(self, text=title, bg=config.COMPONENT_BG, fg=config.TEXT_COLOR, 
                 font=config.FONT_MAIN).pack(pady=5)
        
        self.content_frame = tk.Frame(self, bg=config.COMPONENT_BG)
        self.content_frame.pack(expand=True)
        
        self.vol_btc_label = tk.Label(self.content_frame, text="Vol(BTC): --", 
                                      bg=config.COMPONENT_BG, fg=config.GREEN_COLOR, font=config.FONT_MAIN)
        self.vol_btc_label.pack(anchor="w")
        
        self.vol_usdt_label = tk.Label(self.content_frame, text="Vol(USDT): --", 
                                       bg=config.COMPONENT_BG, fg=config.RED_COLOR, font=config.FONT_MAIN)
        self.vol_usdt_label.pack(anchor="w")

    def update_data(self, volume_btc, volume_usdt):
        v_btc = float(volume_btc)
        v_usdt = float(volume_usdt)
        
        self.vol_btc_label.config(text=f"Vol: {v_btc:,.2f} BTC")
        self.vol_usdt_label.config(text=f"Val: {v_usdt:,.2f} USDT")