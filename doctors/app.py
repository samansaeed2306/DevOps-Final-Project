from flask import Flask, jsonify, request
from flask_cors import CORS 
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/DevOps"
mongo = PyMongo(app)

# doctors = [
#   { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
#   { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
# ]
@app.route('/hello2.0')
def hello2():
  greeting = "Hello Doctors 2.0!"
  return greeting

@app.route('/hello3')
def hello():
  greeting = "Hello Doctors!"
  return greeting

@app.route('/check_mongodb_connection')
def check_mongodb_connection():
    try:
        mongo.db.doctors.find_one()
        return jsonify({"status": "success", "message": "MongoDB successfully connected "})
    except Exception as e:
        return jsonify({"status": "error", "message": f"MongoDB connection error: {str(e)}"}), 500

@app.route('/doctors', methods=["GET"])
def getDoctors():
  # doctors = list(mongo.db.doctors.find())
  # return jsonify(doctors)
  try:
        doctors = list(mongo.db.doctors.find())

        # Convert ObjectId to string in each document
        for doctor in doctors:
            doctor['_id'] = str(doctor['_id'])

        return jsonify(doctors)
  except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
    doctor = mongo.db.doctors.find_one({'id': id})
    return jsonify(doctor)


if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)