import websocket
import threading
import json

class BinanceAPI:
    def __init__(self, callback_func):
        self.ws = None
        self.is_running = False
        self.callback_func = callback_func
        self.ws_url = "wss://stream.binance.com:9443/ws/btcusdt@ticker" 

    def start(self):
        self.is_running = True
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        wst = threading.Thread(target=self.ws.run_forever, daemon=True)
        wst.start()

    def stop(self):
        self.is_running = False
        if self.ws:
            self.ws.close()

    def on_message(self, ws, message):
        if not self.is_running:
            return
        data = json.loads(message)
        self.callback_func(data)

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket Closed")