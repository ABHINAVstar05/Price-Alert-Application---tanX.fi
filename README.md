# Price Alert Application
## tanX.fi backend assignment built using Python-Django and DRF

### DESCRIPTION
**A price alert application that fetches the real-time price of BTC using Binance's WebSocket and triggers an email to users when their target alert_price is achieved.**

### Important features of the project
> 1. Uses **JWT token** for user authentication.
> 2. Uses **Binance's WebSocket** connection to get real-time price updates.
> 3. Triggers an email to users when their target alert_price occurs.
> 4. 5 different **REST API endpoints** for *creating*, *deleting* and *fetching* user's alerts details as per need.

### Steps to SETUP and start a local development environment
1. *Fork* this GitHub repository.
2. Open the terminal and start a Python virtual environment in your local system by
    - creating a virtual environment using `python -m venv virtual_env` and then
    - activating the virtual environment using `virtual_env/Scripts/activate`.
3. *Clone* the *forked* repository to create a local copy of the project files.
4. Install the required dependencies using `python -m pip install -r requirements.txt`.
5. Go to the *project directory* using `cd project`.
6. In **settings.py**, set the *user* and *password* values to your local MySQL user and password values and create a database inside MySQL with name *tanx_alert_application* to set up a local database.
7. Run migrations using `python manage.py makemigrations` and then `python manage.py migrate`.
8. Finally, use the command `python manage.py runserver` to start a local server to use the project.

### Binance's WebSocket running terminal status
|  |
|:--:| 
| *Binance's WebSocket working terminal status* |
> The WebSocket is fetching real-time price update from [wss://stream.binance.com:9443/ws/btcusdt@kline_1s](wss://stream.binance.com:9443/ws/btcusdt@kline_1s).

### REST API endpoints details:
**3 main endpoints are:**
1. A REST API endpoint for the user’s to create an alert at [http://localhost:8000/alerts/create/](http://127.0.0.1:8000/alerts/create/).
2. A REST API endpoint for the user’s to delete an alert at [http://localhost:8000/alerts/delete/](http://127.0.0.1:8000/alerts/delete/).
3. A REST API endpoint to fetch all the alerts that the user has created at [http://localhost:8000/alerts/fetch/](http://127.0.0.1:8000/alerts/fetch/).
    - The response of this API includes the status of the alerts like *CREATED* or *TRIGGERED*.
    - It has an optional filter option based on the status of the alerts. Eg: if the user wants only the alerts that were triggered, then the endpoint would provide just that.

**There are 2 more REST API endpoints:**
1. A REST API endpoint for new user registration or signup at [http://localhost:8000/alerts/signup/](http://127.0.0.1:8000/alerts/signup/).
2. A REST API endpoint for user login using **JWT Token Authentication** at [http://localhost:8000/alerts/login/](http://127.0.0.1:8000/alerts/login/).

### POSTMAN screenshots of all REST APIs responses to different validation conditions on running server 
1. On new user signup/registration at [http://localhost:8000/alerts/signup/](http://127.0.0.1:8000/alerts/signup/).

| ![POSTMAN new user signup success](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/bae16558-9666-495f-a022-03b37508189c) |
|:--:| 
| *POSTMAN new user signup SUCCESS screenshot* |

| ![POSTMAN new user signup PASSWORD REQUIRED VALIDATION](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/1c4acc0c-2831-401c-a828-7e0702604011) |
|:--:| 
| *POSTMAN new user signup PASSWORD REQUIRED VALIDATION screenshot* |

| ![POSTMAN new user signup USER ALREADY EXISTS validation](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/f7d25545-da24-4430-8594-4963d1110cf5) |
|:--:| 
| *POSTMAN new user signup USER ALREADY EXISTS VALIDATION screenshot* |

2. On user login at [http://localhost:8000/alerts/login/](http://127.0.0.1:8000/alerts/login/).

| ![POSTMAN user login success using JWT AUTH](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/1e72cbbf-2f3e-426d-b5ca-e9fc6423d083) |
|:--:| 
| *POSTMAN user login SUCCESS using JWT AUTH screenshot* |

| ![POSTMAN user login PASSWORD VALIDATION using JWT Auth](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/1ee7a822-e7f8-40ce-83f8-2ad4147262d7) |
|:--:| 
| *POSTMAN user login PASSWORD VALIDATION using JWT AUTH screenshot* |

3. On creating a new alert at [http://localhost:8000/alerts/create/](http://127.0.0.1:8000/alerts/create/).

| ![POSTMAN create alert success](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/d836b1ce-e089-477b-81d5-352a998e5419) |
|:--:| 
| *POSTMAN create alert SUCCESS screenshot* |

| ![POSTMAN create alert FOREIGN KEY RELATION CONSTRAINT WITH USER VALIDATION](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/2323d898-61ad-432a-a354-cab4b56dd8f2) |
|:--:| 
| *POSTMAN create alert FOREIGN KEY RELATION CONSTRAINT WITH USER VALIDATION screenshot* |

4. On deleting an alert at [http://localhost:8000/alerts/delete/](http://127.0.0.1:8000/alerts/delete/).

| ![POSTMAN delete alert success](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/49126b30-e33f-4e1f-98a3-6fc607387d2e) |
|:--:| 
| *POSTMAN delete alert SUCCESS screenshot* |

| ![POSTMAN delete alert VALIDATION](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/d90166a1-7296-498a-95ea-b6007d530f34) |
|:--:| 
| *POSTMAN delete alert VALIDATION screenshot* |

5. On fetching a user's alert details at [http://localhost:8000/alerts/fetch/](http://127.0.0.1:8000/alerts/fetch/).

| ![POSTMAN FETCH ALL ALERTS success](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/1cdf933f-3b4a-4012-a8f7-0de97c16d172) |
|:--:| 
| *POSTMAN FETCH ALL ALERTS of a user SUCCESS screenshot* |

| ![POSTMAN FETCH SPECIFIC ALERTS success](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/5b7cd08b-1f3f-4563-923e-07ac7693982a) |
|:--:| 
| *POSTMAN FETCH SPECIFIC ALERTS of a user SUCCESS screenshot* |

### Email triggering terminal status
| ![email trigger terminal status](https://github.com/ABHINAVstar05/Price-Alert-Application---tanX.fi/assets/75786072/9e91fc02-7136-44bd-bc9d-2312bcb082a9) |
|:--:| 
| *Email triggered to the corresponding user terminal status* |
> An email is triggered to the user every time the current BTC price matches the user's set alert price.
