import sys

sys.path.append('/var/www/parking_finder/parking_finder/model')
sys.path.append('/var/www/parking_finder/parking_finder/user_operations')
sys.path.append('/var/www/parking_finder/parking_finder/user')
sys.path.append('/var/www/parking_finder/parking_finder/database')

from flask import Flask, render_template
import model_app as model
import user_operations_app as user_operations
import user_queries_app as user_queries
import user_app as user
import connect_database as db_connection

db = db_connection.connect()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    return model.find()


@app.route('/<string:collection>/add', methods=['POST'])
def add_document(collection):
    return user_operations.create(collection, db)


@app.route('/<string:collection>/get', methods=['GET'])
def get_document(collection):
    return user_operations.get(collection, db)


@app.route('/<string:collection>/update', methods=['PUT'])
def update_document(collection):
    return user_operations.update(collection, db)


@app.route('/<string:collection>/delete', methods=['DELETE'])
def delete_document(collection):
    return user_operations.delete(collection, db)


@app.route('/show_garage_reviews', methods=['GET'])
def show_garage_reviews():
    return user_queries.show_garage_reviews(db)


@app.route('/show_street_reviews', methods=['GET'])
def show_street_reviews():
    return user_queries.show_street_reviews(db)


@app.route('/get_owner_garages', methods=['GET'])
def get_owner_garages():
    return user_queries.get_owner_garages(db)


@app.route('/get_user_bookmark', methods=['GET'])
def get_user_bookmark():
    return user_queries.get_user_bookmark(db)


@app.route('/sign_up', methods=['POST'])
def sign_up():
    return user.sign_up(db)


@app.route('/update_name', methods=['POST'])
def update_name():
    return user.update_name()


@app.route('/update_email', methods=['POST'])
def update_email():
    return user.update_email()


@app.route('/update_password', methods=['POST'])
def update_password():
    return user.update_password()


@app.route('/update_number', methods=['POST'])
def update_number():
    return user.update_number()


@app.route('/get_by_email', methods=['GET'])
def get_by_mail():
    return user.get_by_mail()


@app.route('/get_by_id', methods=['GET'])
def get_by_id():
    return user.get_by_id()


@app.route('/log_in', methods=['GET'])
def log_in():
    return user.log_in()
