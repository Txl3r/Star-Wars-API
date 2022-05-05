"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planets, Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/people', methods=['GET'])
def handle_person():

    people = People.query.all()
    people_list = list(map(lambda x: x.serialize(), people))
    return jsonify(people_list), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def handle_each_person(people_id):

    people = People.query.get(people_id)

    return jsonify(person), 200

@app.route('/people', methods=['POST'])
def create_people():

    request_body = request.get_json()
    new_people = People(email=request_body['email'], password=request_body['password'], is_active=request_body['is_active'])
    db.session.add(new_people)
    db.session.commit()
    return f"The new people {request_body['email']} was created successfully", 200

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people():
    people = people.query,get(people_id)
    if people is None:
        raise APIException('People not found', status_code=404)
    db.session.delete(people)
    db.session.commit()

@app.route('/planets', methods=['GET'])
def handle_planets():

    planet = Planets.query.all()
    planet_list = list(map(lambda i: i.serialize(), planet))
    return jsonify(planet_list), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_each_planet(planet_id):
    planet = Planets.query.get(planet_id)
    return planets.serialize(), 200

@app.route('/planets', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planets(planet_name=request_body['planet_name'], climate=request_body['climate'], gravity=request_body['gravity'], population=request_body['population'])
    db.session.add(new_planet)
    db.session.commit()
    return f"The new planet {request_body['planet_name']} was created successfully", 200

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    pass

@app.route('/characters', methods=['GET'])
def handle_characters():

    character = Characters.query.all()
    character_list = list(map(lambda c: c.serialize(), character))
    return jsonify(character_list), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def handle_each_character(character_id):

    character = Characters.query.get(character_id)

    return jsonify(character), 200

@app.route('/characters', methods=["POST"])
def create_characters():

    request_body = request.get_json()
    new_character = Characters(character_name=request_body['character_name'], height=request_body['height'], age=request_body['age'], hair_color=request_body['hair_color'], eye_color=request_body['eye_color'])
    db.session.add(new_character)
    db.session.commit()
    return f"The new character {request_body['character_name']} was created successfully", 200

@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):

    pass
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
