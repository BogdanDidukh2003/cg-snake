import pygame as pg
import pygame_widgets as pgw
from src.constants import FONT, BUTTON_FONT_SIZE, COLORS, BUTTON_RADIUS, BUTTON_MARGIN, PAUSE_TRANSPARENCY


class Pause:
    def __init__(self, screen: pg.Surface, continue_callback, text='PAUSE'):
        self.screen = screen
        self.surface = pg.Surface(screen.get_size())
        self.surface = self.surface.convert()
        self.surface.set_alpha(int(PAUSE_TRANSPARENCY * 255))
        self.title_font = pg.font.SysFont(FONT, BUTTON_FONT_SIZE)
        self.title = self.title_font.render(text, True, COLORS['SCORE_TEXT_COLOR'])

        width, height = self.screen.get_size()
        element_height = int(height * (1 / 7))
        element_width = int(width * 0.25)
        self.continue_button = pgw.Button(
            self.screen,
            (width - element_width) // 2,
            height - int(element_height * 3.5),
            element_width,
            element_height,
            text='CONTINUE',
            fontSize=BUTTON_FONT_SIZE,
            margin=BUTTON_MARGIN,
            inactiveColour=COLORS['BUTTON'],
            pressedColour=COLORS['BUTTON_PRESSED'],
            radius=BUTTON_RADIUS,
            onClick=continue_callback,
        )

        self.coordinates = (width // 4, height // 4)
        self.size = (width // 2, height // 2)
        self.area = pg.Rect(self.coordinates, self.size)

    def __render_title(self):
        width, height = self.screen.get_size()
        self.screen.blit(self.title,
                         (width // 2 - self.title.get_size()[0] // 2,
                          height // 2 - self.title.get_size()[1] * 3))

    def render(self, events):
        self.screen.blit(self.surface, self.coordinates, area=self.area)
        self.surface.fill(COLORS['MAIN_BACKGROUND'])
        self.__render_title()
        self.continue_button.listen(events)
        self.continue_button.draw()
