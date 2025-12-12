import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
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
        self.ax.set_title("BTC/USDT 1 Minute Chart", color='white')
        self.times = []
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_candle(self, timestamp, open_p, high_p, low_p, close_p):
        dt = datetime.fromtimestamp(timestamp / 1000)
        if len(self.times) > 0 and self.times[-1] == dt:
            self.closes[-1] = close_p
            self.highs[-1] = max(self.highs[-1], high_p)
            self.lows[-1] = min(self.lows[-1], low_p)
        else:
            self.times.append(dt)
            self.opens.append(open_p)
            self.highs.append(high_p)
            self.lows.append(low_p)
            self.closes.append(close_p)
            
            if len(self.times) > 30: 
                self.times.pop(0)
                self.opens.pop(0)
                self.highs.pop(0)
                self.lows.pop(0)
                self.closes.pop(0)
        self.draw_chart()

    def draw_chart(self):
        self.ax.clear() #
        self.ax.plot(self.times, self.closes, color=config.GREEN_COLOR, linewidth=2)
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.fig.autofmt_xdate()
        
        self.canvas.draw()