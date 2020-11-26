import pygame as pg
from src.constants import NUM_BLOCKS, COLORS, DIRECTION
from src.exceptions import SnakeDeath
from src.logic import get_block_rect, is_position_allowed, format_position, set_score


class Snake:
    def __init__(self, speed=1., init_score=0,
                 init_position=(NUM_BLOCKS[0] // 2, NUM_BLOCKS[1] // 2)):
        self.__score = init_score
        self.__speed = 0
        self.__color = (0, 0, 0)
        self.set_speed(speed)
        self.__length = 1
        self.__border_color = COLORS['ADDITIONAL_BACKGROUND']
        self.__positions = [format_position(init_position)]
        self.__direction = DIRECTION['STOP']
        self.__is_acceleration = False

    @property
    def score(self):
        return self.__score

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    @property
    def positions(self):
        return self.__positions

    @property
    def speed(self):
        return self.__speed + (0.5 if self.__is_acceleration else 0)

    def set_speed(self, speed):
        if speed < 0:
            speed = 1.
        if speed < 1.:
            self.__color = COLORS['SNAKE_SLOW']
        elif speed == 1.:
            self.__color = COLORS['SNAKE_MEDIUM']
        else:
            self.__color = COLORS['SNAKE_FAST']
        self.__speed = speed

    def get_head_position(self):
        return self.__positions[0]

    def change_direction(self, direction):
        if not (self.__length > 1 and (direction[0] * -1, direction[1] * -1) == self.__direction):
            self.__direction = direction

    def move(self):
        if self.__direction == DIRECTION['STOP']:
            return
        x, y = self.get_head_position()
        new_head_position = format_position((x + self.__direction[0], y + self.__direction[1]))
        if is_position_allowed(new_head_position, self.__positions):
            self.__positions.insert(0, new_head_position)
        else:
            set_score(self.__score)
            raise SnakeDeath

    def set_acceleration(self, is_acceleration):
        self.__is_acceleration = is_acceleration

    def increment_score(self, value):
        self.__score += value

    def render(self, surface):
        if len(self.__positions) > self.__length:
            self.__positions.pop()

        x, y = self.get_head_position()
        shape = get_block_rect(x, y)
        pg.draw.rect(surface, COLORS['SNAKE_HEAD'], shape)
        pg.draw.rect(surface, self.__border_color, shape, 1)

        if len(self.__positions) > 1:
            for (x, y) in self.__positions[1:]:
                shape = get_block_rect(x, y)
                pg.draw.rect(surface, self.__color, shape)
                pg.draw.rect(surface, self.__border_color, shape, 1)
