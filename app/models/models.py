from pydantic import BaseModel, Field
from enum import Enum
from app.constants.constants import TABLE_SIZE

class Direction(str, Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

class PlaceCommand(BaseModel):
    x: int = Field(ge=0, lt=TABLE_SIZE)
    y: int = Field(ge=0, lt=TABLE_SIZE)
    f: Direction

class RobotState:
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None
        self.is_placed = False

    def place(self, x: int, y: int, f: Direction):
        if 0 <= x < TABLE_SIZE and 0 <= y < TABLE_SIZE:
            self.x = x
            self.y = y
            self.f = f
            self.is_placed = True

    def move(self):
        if not self.is_placed:
            return

        if self.f == Direction.NORTH and self.y < TABLE_SIZE - 1:
            self.y += 1
        elif self.f == Direction.SOUTH and self.y > 0:
            self.y -= 1
        elif self.f == Direction.EAST and self.x < TABLE_SIZE - 1:
            self.x += 1
        elif self.f == Direction.WEST and self.x > 0:
            self.x -= 1

    def left(self):
        if not self.is_placed:
            return

        directions = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
        self.f = directions[(directions.index(self.f) + 1) % len(directions)]

    def right(self):
        if not self.is_placed:
            return

        directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        self.f = directions[(directions.index(self.f) + 1) % len(directions)]

    def report(self):
        if not self.is_placed:
            return {"error": "Robot not placed on the table."}
        return {"x": self.x, "y": self.y, "f": self.f}