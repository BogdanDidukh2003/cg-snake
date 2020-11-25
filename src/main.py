import pygame as pg

from src.constants import FPS, SCREEN_SIZE, TITLE, DIRECTION, DEFAULT_SPEED, \
    SLOW_SPEED, MEDIUM_SPEED, FAST_SPEED, TIME_TO_START_ACCELERATION_MS
from src.exceptions import SnakeDeath
from src.screens import Gameplay, Menu, BestScore


def mainloop():
    fps_clock = pg.time.Clock()
    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)

    is_running = True
    is_main_menu = True
    is_best_score = False
    is_select_speed_menu = False
    is_game = False

    is_speed_selected = False
    direction = DIRECTION['STOP']
    snake_speed = MEDIUM_SPEED

    keypress_start = pg.time.get_ticks()
    key_is_pressed = False
    accelerate_snake = False

    def start_button_callback():
        nonlocal is_select_speed_menu
        is_select_speed_menu = True

    def best_score_button_callback():
        nonlocal is_best_score
        is_best_score = True

    def quit_button_callback():
        nonlocal is_running
        is_running = False

    main_menu = Menu(screen,
                     ('START', 'BEST_SCORE', 'QUIT'),
                     first_button_callback=start_button_callback,
                     second_button_callback=best_score_button_callback,
                     third_button_callback=quit_button_callback)

    def slow_button_callback():
        nonlocal snake_speed, is_speed_selected
        snake_speed = SLOW_SPEED
        is_speed_selected = True

    def medium_button_callback():
        nonlocal snake_speed, is_speed_selected
        snake_speed = MEDIUM_SPEED
        is_speed_selected = True

    def fast_button_callback():
        nonlocal snake_speed, is_speed_selected
        snake_speed = FAST_SPEED
        is_speed_selected = True

    select_speed_screen = Menu(screen,
                               ('SLOW', 'MEDIUM', 'HIGH'),
                               first_button_callback=slow_button_callback,
                               second_button_callback=medium_button_callback,
                               third_button_callback=fast_button_callback,
                               is_vertical=False)

    def back_button_callback():
        nonlocal is_best_score, is_main_menu
        is_best_score = False
        is_main_menu = True

    best_score_screen = BestScore(screen,
                                  back_button_callback=back_button_callback)
    gameplay = None

    while is_running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    direction = DIRECTION['UP']
                    keypress_start = pg.time.get_ticks()
                    key_is_pressed = True
                elif event.key == pg.K_DOWN:
                    direction = DIRECTION['DOWN']
                    keypress_start = pg.time.get_ticks()
                    key_is_pressed = True
                elif event.key == pg.K_LEFT:
                    direction = DIRECTION['LEFT']
                    keypress_start = pg.time.get_ticks()
                    key_is_pressed = True
                elif event.key == pg.K_RIGHT:
                    direction = DIRECTION['RIGHT']
                    keypress_start = pg.time.get_ticks()
                    key_is_pressed = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    key_is_pressed = False
                    accelerate_snake = False
                elif event.key == pg.K_DOWN:
                    key_is_pressed = False
                    accelerate_snake = False
                elif event.key == pg.K_LEFT:
                    key_is_pressed = False
                    accelerate_snake = False
                elif event.key == pg.K_RIGHT:
                    key_is_pressed = False
                    accelerate_snake = False

        if is_main_menu:
            main_menu.render(events)
        if is_select_speed_menu:
            is_main_menu = False
            select_speed_screen.render(events)
        if is_speed_selected:
            is_select_speed_menu = False
            is_speed_selected = False
            gameplay = Gameplay(screen, init_speed=snake_speed)
            is_game = True
        if is_best_score:
            is_main_menu = False
            best_score_screen.render(events)
        if is_game:
            if key_is_pressed:
                if pg.time.get_ticks() - keypress_start >= TIME_TO_START_ACCELERATION_MS:
                    accelerate_snake = True
            gameplay.snake.set_acceleration(accelerate_snake)

            try:
                gameplay.render(direction=direction)
            except SnakeDeath:
                is_game = False
                is_main_menu = True

        pg.display.update()
        if is_game:
            fps_clock.tick(int(gameplay.snake.speed * DEFAULT_SPEED))
        else:
            fps_clock.tick(FPS)
