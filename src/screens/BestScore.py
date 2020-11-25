import pygame as pg
import pygame_widgets as pgw
from src.constants import COLORS, BUTTON_FONT_SIZE, FONT, BUTTON_MARGIN, BUTTON_RADIUS
from src.logic import get_best_score


class BestScore:
    def __init__(self, screen, back_button_callback):
        self.screen = screen
        self.surface = pg.Surface(screen.get_size())
        self.surface = self.surface.convert()
        self.best_score_font = pg.font.SysFont(FONT, BUTTON_FONT_SIZE)
        self.title = self.best_score_font.render('BEST SCORE', True, COLORS['SCORE_TEXT_COLOR'], )
        self.value = get_best_score()

        width, height = self.screen.get_size()
        element_height = int(height * (1 / 7))
        element_width = int(width * 0.25)
        self.back_button = pgw.Button(
            self.screen,
            (width - element_width) // 2,
            height - int(element_height * 1.5),
            element_width,
            element_height,
            text='BACK',
            fontSize=BUTTON_FONT_SIZE,
            margin=BUTTON_MARGIN,
            inactiveColour=COLORS['BUTTON'],
            pressedColour=COLORS['BUTTON_PRESSED'],
            radius=BUTTON_RADIUS,
            onClick=back_button_callback,
        )

    def __render_score(self):
        width, height = self.screen.get_size()
        character_width = self.title.get_size()[0] // len('BEST SCORE')
        self.screen.blit(self.title,
                         (width // 2 - self.title.get_size()[0] // 2,
                          height // 2 - self.title.get_size()[1] * 2))
        value = f'{get_best_score()}'
        score = self.best_score_font.render(value, True, COLORS['SCORE_TEXT_COLOR'], )
        self.screen.blit(score, (width // 2 - int(character_width * len(value) / 2), height // 2))

    def render(self, events):
        self.screen.blit(self.surface, (0, 0))
        self.surface.fill(COLORS['MAIN_BACKGROUND'])
        self.__render_score()
        self.back_button.listen(events)
        self.back_button.draw()
