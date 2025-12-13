import websocket
import threading
import json
from utils import config

class BinanceAPI: 
    def __init__(self, callback_func):
        self.ws = None
        self.is_running = False
        self.callback_func = callback_func
        self.current_symbol = "btcusdt"

    def start(self,symbol="btcusdt"):
        self.stop()
        
        self.current_symbol = symbol.lower()
        ws_url = config.BASE_WS_URL.format(symbol=self.current_symbol)
        
        self.is_running = True
        self.ws = websocket.WebSocketApp(
            ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        threading.Thread(target=self.ws.run_forever, daemon=True).start()

    def stop(self):
        self.is_running = False
        if self.ws:
            self.ws.close()

    def on_message(self, ws, message):
        if not self.is_running: return
        data = json.loads(message)
        self.callback_func(data)

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status, close_msg):
        print("WebSocket Closed")