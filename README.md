# Price Alert Application
## tanX.fi backend assignment built using Python-Django and DRF

### DESCRIPTION:-
**A price alert application that fetches real-time price of BTC using Binance's WebSocket and triggers an email to users when their target alert_price is achieved.**

### Important features of the project:-
> 1. Uses **JWT token** for user authentication.
> 2. Uses **Binance's WebSocket** connection to get real-time price updates.
> 3. Triggers an email to users when their target alert_price occurs.
> 4. 3 different **REST API endpoints** for *creating*, *deleting* and *fetching* user's alerts details as per need.

### Steps to SETUP and start a local development environment
1. *Fork* this GitHub repository.
2. Open terminal and start a python virtual environment in your local system by
    - creating a virtual environment using `python -m venv virtual_env` and then
    - activating the virtual environment using `virtual_env/Scripts/activate`.
3. *Clone* the *forked* repository to create a local copy of the project files.
4. Install the required dependencies using `python -m pip install -r requirements.txt`.
5. Go to the *project directory* using `cd project`.
6. In **settings.py**, set the *user* and *password* values to your local MySQL user and password values and create a database inside MySQL with name *tanx_alert_application* to setup a local database for use.
7. Run migrations using `python manage.py makemigrations` and then `python manage.py migrate`.
8. Finally, use the command `python manage.py runserver` to start a local server to use the project.
