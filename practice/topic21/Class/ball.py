import pygame.draw

from topic21.Class.vector import Vector

EXAMPLES = []


class Ball:

    def __init__(self, sc, pos, color, radius, speed):
        EXAMPLES.append(self)
        self.sc = sc
        self.pos = Vector(*pos)
        self.color = color
        self.radius = radius
        self.speed = Vector(*speed)

    def __bool__(self):
        return True

    def update(self):
        new_pos = self.pos + self.speed
        new_speed = self.speed
        if new_pos.x <= self.radius:
            new_pos = Vector(abs(self.pos.x + self.speed.x), self.pos.y + self.speed.y)
            new_speed = Vector(-self.speed.x, self.speed.y)
        elif new_pos.x >= self.sc.get_size()[0]:
            new_pos = Vector(2 * self.sc.get_size()[0] - new_pos.x, self.pos.y + self.speed.y)
            new_speed = Vector(-self.speed.x, self.speed.y)
        if new_pos.y <= self.radius:
            new_pos = Vector(new_pos.x, abs(new_pos.y))
            new_speed = Vector(new_speed.x, - new_speed.y)
        elif new_pos.y >= self.sc.get_size()[1]:
            new_pos = Vector(new_pos.x, 2 * self.sc.get_size()[1] - new_pos.y)
            new_speed = Vector(new_speed.x, - new_speed.y)
        self.pos = new_pos
        self.speed = new_speed

    def render(self):
        pygame.draw.circle(self.sc, self.color, self.pos.intpair(), self.radius)

    def clash(self, other):
        return abs(self.pos.x - other.pos.x) <= self.radius + other.radius and\
               abs(self.pos.y - other.pos.y) <= self.radius + other.radius

    # task6
    def push_off(self, other):
        m1 = self.radius ** 2
        m2 = other.radius ** 2
        x = ((self.speed * (m1 - m2)) + (2 * m2 * other.speed)) / (m1 + m2)
        y = ((other.speed * (m2 -m1)) + (2 * m1 * self.speed)) / (m1 + m2)
        self.speed, other.speed = x, y

    @staticmethod
    def get_all_ball():
        return EXAMPLES

#DONE
