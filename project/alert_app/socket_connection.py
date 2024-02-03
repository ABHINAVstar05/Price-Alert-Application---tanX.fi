import websocket
import json

""" A python function to fetch real-time current prices of BTC using Binance's websocket """
def get_prices() :
    socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1s'

    def on_message(ws, message):
        data = json.loads(message)
        if 'k' in data:
            data = data['k']
            if 'c' in data :
                print("Current price:", data['c'])
            else:
                print('Something unexpected occured.')
        else:
            print('Something unexpected occured.')

    ws = websocket.WebSocketApp(socket, on_message = on_message)
    ws.run_forever()

get_prices()
