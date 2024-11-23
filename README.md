To start server:
1. install python3
2. Create virtual environment
    (mac) python3 -m venv .venv
    (windows) py -m venv .venv
3. Activate virtual environment
    (mac) source .venv/bin/activate
    (windows) source .venv/Script/activate
4. Go to project location
    cd back_zero
5. install dependensies
    pip install Django
    (also install Pillow and the other libraries)
6. migrate models
    (mac) python3 manage.py migrate
    (windows) py manage.py migrate
7. start server
    (mac) python3 manage.py runserver
    (windows) py manage.py runserver

To stop server:
1. CTRL + c
2. exit venv
    (mac | windows) deactivate