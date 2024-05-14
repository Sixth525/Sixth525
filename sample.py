import requests

api_url = "http://127.0.0.1:5000/generate_employee_locations_map"

response = requests.get(api_url)


if response.status_code == 200:
    print("Map created successfully!")
else:
    print("Failed to create map:", response.text)

from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John Doe", "position": "Software Engineer", "department": "Engineering"},
    {"id": 2, "name": "Jane Smith", "position": "HR Manager", "department": "Human Resources"},
    {"id": 3, "name": "Alice Johnson", "position": "Marketing Specialist", "department": "Marketing"}
]

@app.route('/api/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/api/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((emp for emp in employees if emp['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/api/employees', methods=['POST'])
def create_employee():
    data = request.json
    if 'name' in data and 'position' in data and 'department' in data:
        data['id'] = len(employees) + 1
        employees.append(data)
        return jsonify(data), 201
    else:
        return jsonify({"error": "Incomplete employee data"}), 400

if __name__ == '__main__':
    app.run(debug=True)