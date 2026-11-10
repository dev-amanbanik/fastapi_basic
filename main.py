from fastapi import FastAPI,HTTPException
import json

app = FastAPI()
  
@app.get("/")                     # Endpoint -> where on the URL the below message must be displayed
def home():
  return {"how are you this is home page"}

@app.get("/hello")
def hello():
  return "Hello, World! this is hello function"

def load_data():                  # helper function to read the data from the json file
   with open("students.json", "r") as file:
       return json.load(file)

@app.get("/student")   
def students():
    data = load_data()
    return data

# student_id ->  this is our path parameter.
@app.get("/student/{student_id}")
def get_id(student_id: str):
   data=load_data()
   if student_id not in data:
       raise HTTPException(
          status_code=404,
          detail=f"Student id {student_id} not found")
   return data[student_id]