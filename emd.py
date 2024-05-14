from fastapi import FastAPI
import folium
import requests
from IPython.display import display

app = FastAPI()
def get_employee_locations():
    api_url = "http://127.0.0.1:8000/api/employees" 
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_map():
    employee_locations = get_employee_locations()
    if employee_locations:
        map = folium.Map(location=[37.7749, -122.4194], zoom_start=5)
        for employee in employee_locations:
            folium.Marker(location=[employee['latitude'], employee['longitude']], popup=employee['name']).add_to(map)
        #map.save('employees.html')
        display(map)

        return True
    else:
        return False


@app.get('/generate_employee_locations_map')
def generate_employee_locations_map():
    map_emp = create_map()
    if map_emp:
        #return {"message": "Map created successfully!"}
        return map_emp._repr_html_()
    else:
        return {"error": "Failed to create map or fetch employee locations."}