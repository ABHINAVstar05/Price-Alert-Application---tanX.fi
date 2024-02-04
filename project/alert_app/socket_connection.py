import json
import asyncio
import websockets
from asgiref.sync import sync_to_async
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from .api_views import *

# Function to send email to users on alert_price match.
def trigger_email(email):
    send_mail(
        "Target Price Alert Reached!!!",
        "Dear user, with great pleasure, the current_price of BTC matched with your alert_price. Kindly take appropriate steps.",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently = False,
    )

# A function to check if the current_price matches alert_price of any user.
# If yes, then trigger an email to that user using model.trigger_email() function.

@sync_to_async
def compare_prices(current_price) :
    if Alert.objects.filter(alert_price = current_price) :
    
        alerts = Alert.objects.filter(alert_price = current_price)

        for obj in alerts.iterator() :
            user_email = obj.username.email
            print('\nTEST HIT OCCURED. \nAn email is triggered to', user_email,'\n')
            trigger_email(user_email)


# Below functions are related to the Binance's WebSocket.
            
async def websocket_listener(websocket):
    async for message in websocket:
        data = json.loads(message)

        if 'k' in data:
            data = data['k']

            if 'c' in data :
                current_price = data['c']
                
                await compare_prices(current_price) # calling compare_prices() to simultaneously to check for current_price == alert_price
                
                print("Current price:", current_price)

            else:
                print('Something unexpected occured.')
        else:
            print('Something unexpected occured.')
    await asyncio.sleep(2)


async def main():
    socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1s'
    async with websockets.connect(socket) as wb:
        await asyncio.gather(
            websocket_listener(wb)
        )

asyncio.run(main())
