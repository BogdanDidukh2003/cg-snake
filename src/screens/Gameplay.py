import pygame as pg

from src.components import Snake, Snack
from src.constants import COLORS, FONT, FONT_SIZE, NUM_BLOCKS
from src.logic import get_block_rect


class Gameplay:
    def __init__(self, screen: pg.Surface, init_speed=1.):
        self.screen = screen
        self.surface = pg.Surface(screen.get_size())
        self.surface = self.surface.convert()

        self.score_font = pg.font.SysFont(FONT, FONT_SIZE)

        self.snake = Snake(speed=init_speed)
        self.snack = Snack(self.snake)

    def __render_background(self):
        width, height = NUM_BLOCKS
        for x in range(width):
            for y in range(height):
                shape = get_block_rect(x, y)
                if (x + y) % 2:
                    pg.draw.rect(self.surface, COLORS['MAIN_BACKGROUND'], shape)
                else:
                    pg.draw.rect(self.surface, COLORS['ADDITIONAL_BACKGROUND'], shape)

    def __render_score(self):
        text = self.score_font.render(f'Score {self.snake.score}', True, COLORS['SCORE_TEXT_COLOR'])
        self.screen.blit(text, (10, 10))

    def __render_snack(self):
        self.snack.render(self.surface)

    def __render_snake(self):
        self.snake.render(self.surface)

    def render(self, **kwargs):
        self.screen.blit(self.surface, (0, 0))
        self.surface.fill(COLORS['MAIN_BACKGROUND'])
        self.__render_background()

        if 'direction' in kwargs:
            self.snake.change_direction(kwargs['direction'])
        if 'level' in kwargs:
            self.snake.update_level(kwargs['level'])
        if 'speed_bonus' in kwargs:
            self.snake.set_speed_bonus(kwargs['speed_bonus'])
        else:
            self.snake.set_speed_bonus()

        self.snake.move()

        if self.snake.get_head_position() == self.snack.position:
            self.snake.length = self.snake.length + 1
            self.snake.increment_score(self.snack.value)
            if 'snack_bonus' in kwargs and kwargs['snack_bonus']:
                self.snack = Snack(self.snake, init_value=200)
            else:
                self.snack = Snack(self.snake)

        self.__render_snake()
        self.__render_snack()
        self.__render_score()
