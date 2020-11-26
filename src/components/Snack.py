import random
import pygame as pg
from src.constants import COLORS, NUM_BLOCKS, DEFAULT_SCORE_VALUE
from src.logic import get_block_rect


class Snack:
    def __init__(self, snake, init_value=DEFAULT_SCORE_VALUE):
        self.__snake = snake
        self.__position = (0, 0)
        self.__color = COLORS['SNACK']
        self.__assign_position()
        self.__value = init_value

    @property
    def value(self):
        return self.__value

    @property
    def position(self):
        return self.__position

    def __assign_position(self):
        if len(self.__snake.positions) >= (NUM_BLOCKS[0] * NUM_BLOCKS[1]):
            return

        position = random.randrange(NUM_BLOCKS[0]), random.randrange(NUM_BLOCKS[1])
        while position in self.__snake.positions:
            position = random.randrange(NUM_BLOCKS[0]), random.randrange(NUM_BLOCKS[1])
        self.__position = position

    def render(self, surface):
        x, y = self.__position
        shape = get_block_rect(x, y)
        pg.draw.rect(surface, self.__color, shape)
