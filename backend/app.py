from flask import Flask, request, jsonify
from flask_cors import CORS

import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parusha#20",  
        database="blood_bank_db"
    )

@app.route('/')
def home():
    return "Blood Bank Management System API is running."


@app.route('/add_donor', methods=['POST'])
def add_donor():
    data = request.get_json()
    name = data['name']
    blood_type = data['blood_type']
    contact_info = data['contact_info']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, blood_type, contact_info) VALUES (%s, %s, %s)",
                   (name, blood_type, contact_info))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Donor added successfully!'})

@app.route('/add_request', methods=['POST'])
def add_request():
    data = request.get_json()
    blood_type = data['blood_type']
    quantity = data['quantity']
    requestor_name = data['requestor_name']
    contact_info = data['contact_info']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blood_requests (blood_type, quantity, requestor_name, contact_info) VALUES (%s, %s, %s, %s)",
                   (blood_type, quantity, requestor_name, contact_info))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Blood request added successfully!'})


@app.route('/donors', methods=['GET'])
def get_donors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(donors)

@app.route('/blood_requests', methods=['GET'])
def get_blood_requests():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM blood_requests")
    requests = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(requests)

if __name__ == '__main__':
    app.run(debug=True)

