from fastapi import FastAPI
import emd
app = FastAPI()

employees = [
    {"name": "Alice", "latitude": 37.7749, "longitude": -122.4194},
    {"name": "Bob", "latitude": 34.0522, "longitude": -118.2437},
    {"name": "Charlie", "latitude": 40.7128, "longitude": -74.0060}
]

@app.get('/api/employees')
def get_employees():
    return employees

@app.get('/api/employees/{id}')
def get_employee(id: int):
    if id < len(employees):
        return employees[id]
    else:
        return {"error": "Employee not found"}

@app.post('/api/employees')
def create_employee(employee: dict):
    if 'name' not in employee or 'latitude' not in employee or 'longitude' not in employee:
        return {"error": "Incomplete employee data"}
    employees.append(employee)
    return employee
