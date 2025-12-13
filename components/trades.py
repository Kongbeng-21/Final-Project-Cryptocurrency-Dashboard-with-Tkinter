import tkinter as tk
from tkinter import ttk
from utils import config
from datetime import datetime

class RecentTrades(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=config.COMPONENT_BG)
        
        tk.Label(self, text="Recent Trades", bg=config.COMPONENT_BG, fg="white").pack(pady=5)
        
        columns = ("time", "price", "qty")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)
        
        self.tree.heading("time", text="Time")
        self.tree.heading("price", text="Price")
        self.tree.heading("qty", text="Qty")
        
        self.tree.column("time", width=80)
        self.tree.column("price", width=80)
        self.tree.column("qty", width=80)
        
        self.tree.pack(fill="both", expand=True)
        
        self.tree.tag_configure("buy", foreground=config.GREEN_COLOR, background=config.COMPONENT_BG)
        self.tree.tag_configure("sell", foreground=config.RED_COLOR, background=config.COMPONENT_BG)

    def add_trade(self, time_ms, price, qty, is_buyer_maker):
        dt = datetime.fromtimestamp(time_ms / 1000).strftime('%H:%M:%S')
        side = "sell" if is_buyer_maker else "buy"
        self.tree.insert("", 0, values=(dt, f"{float(price):,.2f}", float(qty)), tags=(side,))
    
        if len(self.tree.get_children()) > 20:
            self.tree.delete(self.tree.get_children()[-1])