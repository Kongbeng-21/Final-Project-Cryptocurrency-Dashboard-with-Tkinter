import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
from utils import config

class Chart(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=config.COMPONENT_BG)
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.fig.patch.set_facecolor(config.COMPONENT_BG) 
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor(config.BACKGROUND_COLOR)  
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.3) 
        self.candles = [] 
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_candle(self, timestamp, open_p, high_p, low_p, close_p):
        dt_str = datetime.fromtimestamp(timestamp / 1000).strftime('%H:%M')
        
        new_candle = {
            "time": dt_str,
            "open": open_p,
            "high": high_p,
            "low": low_p,
            "close": close_p,
            "ts": timestamp 
        }

        if len(self.candles) > 0 and self.candles[-1]['ts'] == timestamp:
            self.candles[-1] = new_candle
        else:
            self.candles.append(new_candle)
            if len(self.candles) > 30:
                self.candles.pop(0)

        self.draw_chart()

    def draw_chart(self):
        self.ax.clear() 
        self.ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.3) 
        
        if not self.candles:
            self.canvas.draw()
            return

        indices = range(len(self.candles)) 
        opens = [c['open'] for c in self.candles]
        closes = [c['close'] for c in self.candles]
        highs = [c['high'] for c in self.candles]
        lows = [c['low'] for c in self.candles]

        up_indices = []
        down_indices = []
        colors = []
        
        for i, c in enumerate(self.candles):
            if c['close'] >= c['open']:
                up_indices.append(i)
                colors.append(config.GREEN_COLOR)
            else:
                down_indices.append(i)
                colors.append(config.RED_COLOR)
        self.ax.vlines(indices, lows, highs, color=colors, linewidth=1)

        for i in indices:
            o = opens[i]
            c = closes[i]
            color = colors[i]
            height = c - o
            if height == 0: height = 0.01 
            
            self.ax.bar(i, height, bottom=o, color=color, width=0.6)
            
        if len(self.candles) < 10:
            self.ax.set_xlim(-1, 10)
        else:
            self.ax.set_xlim(min(indices)-1, max(indices)+1)
            
        step = max(1, len(self.candles) // 6)
        shown_indices = indices[::step]
        shown_labels = [self.candles[i]['time'] for i in shown_indices]
        
        self.ax.set_xticks(shown_indices)
        self.ax.set_xticklabels(shown_labels, rotation=0, color='white', fontsize=8)

        symbol_title = "Price Chart"
        if hasattr(self.master, 'current_coin'): 
             symbol_title = f"{self.master.current_coin} Chart"
             
        self.ax.set_title(symbol_title, color='white', fontsize=10)
        
        self.canvas.draw()