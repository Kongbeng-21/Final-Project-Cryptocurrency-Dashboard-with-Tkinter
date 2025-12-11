import tkinter as tk
from utils import config

class PriceCard(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg=config.COMPONENT_BG)
        self.price_label = tk.Label(self, text="Loading...", bg=config.COMPONENT_BG, fg=config.TEXT_COLOR, font=config.FONT_LARGE)
        self.price_label.pack()

    def update_data(self, price, change):
        color = config.GREEN_COLOR if float(change) >= 0 else config.RED_COLOR
        self.price_label.config(text=f"${float(price):,.2f}", fg=color)
