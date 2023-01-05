import json
from flask import Flask, request, jsonify
from src.data.model import getFoodTrucksByApplicantName, getExpiredFoodTrucks, getFoodTrucksByStreet, getNearestFoodTrucks, insertFoodTrucksEntity


app = Flask(__name__)


@app.route('/')
def demo():
    return json.dumps({'name': 'Demo App',
                       'purpose': 'Demo'})

@app.route('/api/food/trucks')
def getFoodTrucksByApplicant():
    applicant_name = request.args['applicant']
    return jsonify(getFoodTrucksByApplicantName(applicant_name))

@app.route('/api/food/trucks/expire')
def getExpiredFoodTrucksByDate():
    curr_date = request.args['date']
    return jsonify(getExpiredFoodTrucks(curr_date))

@app.route('/api/search/food/trucks')
def getFoodTrucksStreet():
    street = request.args['street']
    return jsonify(getFoodTrucksByStreet(street))

@app.route('/api/search/food/trucks/geolocation')
def getNerestFoodTrucksByGeoLocation():
    latitude = request.args['latitude']
    longitude = request.args['longitude']
    return jsonify(getNearestFoodTrucks(latitude, longitude))


@app.route('/api/add/food/trucks', methods = ['POST'])
def AddFoodTrucks():
    mp = request.json
    return jsonify(insertFoodTrucksEntity(mp))
   


