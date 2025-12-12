import tkinter as tk
from tkinter import ttk
from utils import config

class OrderBook(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=config.COMPONENT_BG)
        
        header = tk.Label(self, text="Order Book", 
                          bg=config.COMPONENT_BG, fg=config.TEXT_COLOR, font=config.FONT_MAIN)
        header.pack(pady=5)
        columns = ("price", "amount")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)
        self.tree.heading("price", text="Price (USDT)")
        self.tree.heading("amount", text="Amount (BTC)")
        self.tree.column("price", width=100, anchor="e")
        self.tree.column("amount", width=100, anchor="e")
        self.tree.pack(fill="both", expand=True)
        self.tree.tag_configure("bid", foreground=config.GREEN_COLOR, background=config.COMPONENT_BG)
        self.tree.tag_configure("ask", foreground=config.RED_COLOR, background=config.COMPONENT_BG)

    def update_data(self, bids, asks):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for price, amount in reversed(asks[:10]): 
            self.tree.insert("", "end", values=(f"{float(price):,.2f}", f"{float(amount):.5f}"), tags=("ask",))
        self.tree.insert("", "end", values=("---", "---"))
        
        for price, amount in bids[:10]:
            self.tree.insert("", "end", values=(f"{float(price):,.2f}", f"{float(amount):.5f}"), tags=("bid",))