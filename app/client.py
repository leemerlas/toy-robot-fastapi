import requests
from app.constants.constants import BASE_URL

def place(x, y, f):
    response = requests.post(f"{BASE_URL}/PLACE", json={"x": x, "y": y, "f": f})
    print(response.json())

def move():
    response = requests.post(f"{BASE_URL}/MOVE")
    print(response.json())

def left():
    response = requests.post(f"{BASE_URL}/LEFT")
    print(response.json())

def right():
    response = requests.post(f"{BASE_URL}/RIGHT")
    print(response.json())

def report():
    response = requests.get(f"{BASE_URL}/REPORT")
    print(response.json())

if __name__ == "__main__":
    place(0, 0, "NORTH")
    move()
    report()
    left()
    report()
    right()
    move()
    report()
