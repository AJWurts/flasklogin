from flask_login import LoginManager, current_user, login_required, login_user
from passlib.hash import sha256_crypt
from flask import Flask, request
from User import User, getUser

app = Flask(__name__)
app.secret_key = '123124124oihuencjskdbvliuageowl*(@&#HkajO*&BICk&*idwbkacwad'

login_manager = LoginManager()
login_manager.init_app(app)

users = {"ajwurts": User('ajwurts', password='$5$rounds=535000$agHV7i2k5TgDJarw$LPSDOE51jJeYPJrWvcJUsX3bXghT8nSZPDKZvRAANw.')}

cars = {'ajwurts': "Toyota Corolla iM"}

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return users[user_id]
    else:
        return None

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user', methods=['POST'])
def create_user():
    try:
        print("Hello Post User")
        json = request.get_json()
        username = json['username']
        password = json['password']
        password = sha256_crypt.encrypt(password)
        print(username, password)
        user = User(username, password=password)
        users[user.name] = user
        print(user.password);
        return 'true'
    except Exception as e:
        print(e)
        return "false"


@app.route('/login', methods=['POST'])
def user_login():
    try:
        print("Hello Post User")
        json = request.get_json()
        username = json['username']
        password = json['password']
        print(username, password)

        user = users[username]
        if user.check_password(password):
            print("Password Checks Out")
            res = login_user(user, force=True)
            print(res);
            return "true"
        else:
            return "false"
        
    
    except Exception as e:
        print(e)
        return "false"

    
@app.route('/car', methods=['GET'])
@login_required
def get_user_car():
    print(current_user)
    return cars[current_user.name]

@app.route('/car', methods=['PUT'])
@login_required
def add_user_car():
    json = request.get_json()
    car = json['car']
    cars[current_user.name] = car
    return 'true'