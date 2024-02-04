import json
import asyncio
import websockets
from asgiref.sync import sync_to_async

from .models import *

# A function to check if the current_price matches alert_price of any user.
# If yes, then trigger an email to that user using model.trigger_email() function.

@sync_to_async
def compare_prices(current_price) :
    
    print("......CHECKING USER PRICE ALERTS........")
    
    if Alert.objects.filter(alert_price = current_price) :
        print("HIT OBTAINED, PRICES MATCHED")

        alerts = Alert.objects.filter(alert_price = current_price)

        for obj in alerts.iterator() :
            user_id = obj.username
            user = User.objects.get(id = user_id)
            user.trigger_email()

            print('EMAIL TRIGGERED')


# Below functions are related to the Binance's WebSocket.
            
async def websocket_listener(websocket):
    async for message in websocket:
        data = json.loads(message)

        if 'k' in data:
            data = data['k']

            if 'c' in data :
                current_price = data['c']
                
                await compare_prices(current_price) # calling compare_prices() to simultaneously to check for current_price == alert_price
                
                print('*****WORKING*******')
                print("Current price:", current_price)

            else:
                print('Something unexpected occured.')
        else:
            print('Something unexpected occured.')


async def main():
    socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'
    async with websockets.connect(socket) as wb:
        await asyncio.gather(
            websocket_listener(wb)
        )

asyncio.run(main())
