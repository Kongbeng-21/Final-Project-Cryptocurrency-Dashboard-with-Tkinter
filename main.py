import tkinter as tk
from utils.binance_API import BinanceAPI     
from components.ticker import PriceCard      
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
        top_frame = tk.Frame(self.root, bg=config.BACKGROUND_COLOR)
        top_frame.pack(fill="x", padx=10, pady=10)

        self.price_card = PriceCard(top_frame, "Last Traded Price")
        self.price_card.pack(side="left", fill="both", expand=True, padx=5)

    def handle_data(self, data):
        price = data['c']
        change = data['p']
        self.root.after(0, self.price_card.update_data, price, change)

    def on_closing(self):
        self.api.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()