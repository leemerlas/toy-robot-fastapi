from fastapi import FastAPI, HTTPException
from app.models.models import PlaceCommand, RobotState

app = FastAPI()
robot = RobotState()

@app.post("/PLACE")
def place(command: PlaceCommand):
    robot.place(command.x, command.y, command.f)
    return {"status": "Placed"}

@app.post("/MOVE")
def move():
    robot.move()
    return {"status": "Moved"}

@app.post("/LEFT")
def left():
    robot.left()
    return {"status": "Turned left"}

@app.post("/RIGHT")
def right():
    robot.right()
    return {"status": "Turned right"}

@app.get("/REPORT")
def report():
    return robot.report()
