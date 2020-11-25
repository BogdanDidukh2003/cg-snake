import pygame as pg
import pygame_widgets as pgw
from src.constants import COLORS, BUTTON_FONT_SIZE, BUTTON_MARGIN, BUTTON_RADIUS


class Menu:
    def __init__(self, screen: pg.Surface,
                 button_names,
                 first_button_callback,
                 second_button_callback,
                 third_button_callback,
                 is_vertical=True):
        self.screen = screen
        self.surface = pg.Surface(screen.get_size())
        self.surface = self.surface.convert()

        width, height = screen.get_size()
        element_height = int(height * (1 / 7))
        if is_vertical:
            element_width = int(width * 0.45)
            top_left_xs = ((width - element_width) // 2,) * 3
            top_left_ys = (element_height + int(element_height * 0.5),
                           element_height * 3,
                           element_height * 5 - int(element_height * 0.5))
        else:
            element_width = int(width * (1 / 4.6))
            top_left_xs = (int(element_width * 0.4),
                           element_width + 2 * int(element_width * 0.4),
                           element_width * 2 + 3 * int(element_width * 0.4))
            top_left_ys = ((height - element_height) // 2,) * 3

        self.first_button = pgw.Button(
            self.screen, top_left_xs[0], top_left_ys[0], element_width, element_height,
            text=button_names[0],
            fontSize=BUTTON_FONT_SIZE,
            margin=BUTTON_MARGIN,
            inactiveColour=COLORS['BUTTON'],
            pressedColour=COLORS['BUTTON_PRESSED'],
            radius=BUTTON_RADIUS,
            onClick=first_button_callback,
        )
        self.second_button = pgw.Button(
            self.screen, top_left_xs[1], top_left_ys[1], element_width, element_height,
            text=button_names[1],
            fontSize=BUTTON_FONT_SIZE,
            margin=BUTTON_MARGIN,
            inactiveColour=COLORS['BUTTON'],
            pressedColour=COLORS['BUTTON_PRESSED'],
            radius=BUTTON_RADIUS,
            onClick=second_button_callback,
        )
        self.third_button = pgw.Button(
            self.screen, top_left_xs[2], top_left_ys[2], element_width, element_height,
            text=button_names[2],
            fontSize=BUTTON_FONT_SIZE,
            margin=BUTTON_MARGIN,
            inactiveColour=COLORS['BUTTON'],
            pressedColour=COLORS['BUTTON_PRESSED'],
            radius=BUTTON_RADIUS,
            onClick=third_button_callback,
        )

    def render(self, events):
        self.screen.blit(self.surface, (0, 0))
        self.surface.fill(COLORS['MAIN_BACKGROUND'])

        self.first_button.listen(events)
        self.second_button.listen(events)
        self.third_button.listen(events)

        self.first_button.draw()
        self.second_button.draw()
        self.third_button.draw()
