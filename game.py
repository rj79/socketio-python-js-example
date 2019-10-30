from math import pi, sin, cos
from time import monotonic

class Game:
    def __init__(self, size):
        self.angle = 0
        self.angle_velocity = pi / 4
        self.radius = 200
        self.cx = size / 2
        self.cy = size / 2
        self.x = 0
        self.y = 0

    def update(self, dt):
        self.angle += dt * self.angle_velocity
        if self.angle_velocity >= pi:
            self.angle_velocity -= pi
        
        self.x = self.cx + self.radius * cos(self.angle)
        self.y = self.cy + self.radius * sin(self.angle)        
    
    def serialize_state(self):
        return {'time': monotonic(), 'pos': {'x': self.x, 'y': self.y}}
