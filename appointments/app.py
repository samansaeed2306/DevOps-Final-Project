from flask import Flask, jsonify, request
from flask_cors import CORS 
from flask_pymongo import PyMongo
from bson import ObjectId
app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Appointments"
mongo = PyMongo(app)
# appointments = [
#   { 'id': "1",'doctor': "1", 'date': "21 Nov 2023", 'rating':"Good"  },
#   { 'id': "2",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
#   { 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
#   { 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
#   { 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
# ]

@app.route('/hello')
def hello():
  greeting = "Hello hear Appointments!"
  return greeting

@app.route('/check_mongodb_connection')
def check_mongodb_connection():
    try:
        mongo.db.appointments.find_one()
        return jsonify({"status": "success", "message": "MongoDB connection successful"})
    except Exception as e:
        return jsonify({"status": "error", "message": f"MongoDB connection error: {str(e)}"}), 500
@app.route('/health')
def health():
    return jsonify({"status": "ok", "message": "Health check passed"})
    
    
@app.route('/appointments', methods=["GET"])
def getAppointments():
  # return jsonify(appointments)
  try:
        appointments = list(mongo.db.appointments.find())

        # Convert ObjectId to string in each document
        for appointment in appointments:
            appointment['_id'] = str(appointment['_id'])

        return jsonify(appointments)
  except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
  # id = int(id) - 1
  # return jsonify(appointments[id])
  appointment = mongo.db.appointments.find_one({'id': id})
  return jsonify(appointment)

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=6060)
