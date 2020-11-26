import pygame as pg
from src.constants import BLOCK_SHAPE, GRID_SIZE, NUM_BLOCKS, BEST_SCORE_FILE, \
    FONT, TIMER_FONT_SIZE, COLORS


def get_best_score():
    with open(BEST_SCORE_FILE, 'r') as file:
        score = int(file.readline())
    return score


def set_score(new_score):
    with open(BEST_SCORE_FILE, 'r') as file:
        score = int(file.readline())
    if new_score > score:
        with open(BEST_SCORE_FILE, 'w') as file:
            file.write(str(new_score))


def get_block_coordinates(x, y):
    """Get coordinates of block given 2 indices

    :param x: index of block along x axis
    :param y: index of block along y axis
    :return: coordinates of the block
    """
    return x * GRID_SIZE, y * GRID_SIZE


def get_block_rect(x, y):
    """Get Rect object of block given 2 indices

    :param x: index of block along x axis
    :param y: index of block along y axis
    :return: pg.Rect object
    """
    return pg.Rect(get_block_coordinates(x, y), BLOCK_SHAPE)


def is_position_allowed(new_position, positions):
    return not (len(positions) > 1 and new_position in positions)


def format_position(position):
    x, y = position
    x_max, y_max = NUM_BLOCKS[0] - 1, NUM_BLOCKS[1] - 1

    if x > x_max:
        x = 0
    elif x < 0:
        x = x_max
    if y > y_max:
        y = 0
    elif y < 0:
        y = y_max

    return x, y


def render_timer(screen: pg.Surface, seconds, render_background):
    title_font = pg.font.SysFont(FONT, TIMER_FONT_SIZE, bold=True)

    for i in range(seconds, 0, -1):
        title = title_font.render(str(i), True, COLORS['TIMER_TEXT_COLOR'])
        width, height = screen.get_size()
        render_background()
        screen.blit(title,
                    (width // 2 - title.get_size()[0] // 2,
                     height // 2 - title.get_size()[1] // 2))
        pg.display.update()
        pg.time.delay(1000)
