# Author : Muhammad Eid
# This is very simple snake game with python.
# I used curses Library.

import curses
import random

my_screen = curses.initscr()  # Window object to represent the whole screen
curses.curs_set(0)  # To hidden the cursor

screen_height, screen_width = my_screen.getmaxyx()  # The height and the width of the window

my_window = curses.newwin(screen_height, screen_width, 0, 0)  # New window with my dimensions
my_window.keypad(True)  # To use the keyboard
my_window.timeout(100)  # To refresh the window every 100ms

snake_x, snake_y = screen_width//4, screen_height//4  # The snake head start position

snake_body = [  # The body of the snake position
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food_position = [screen_height//2, screen_width//2]  # The food position

my_window.addch(food_position[0], food_position[1], curses.ACS_PI)  # Paint the char on the window

key = curses.KEY_RIGHT  # The move direction of the snake

while True:
    new_key = my_window.getch()
    key = key if new_key == -1 else new_key

    if snake_body[0][0] in [0, screen_height] or snake_body[0][1] in [0, screen_width] or snake_body[0] in snake_body[1:]:
        curses.endwin()
        quit()

    # Snake next move
    new_head = [snake_body[0][0], snake_body[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake_body.insert(0, new_head)

    if snake_body[0] == food_position:
        food_position = None
        while food_position is None:
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food_position = new_food if new_food not in snake_body else None
        my_window.addch(food_position[0], food_position[1], curses.ACS_PI)
    else:
        snake_tail = snake_body.pop()
        my_window.addch(snake_tail[0], snake_tail[1], ' ')

    my_window.addch(snake_body[0][0], snake_body[0][1], curses.ACS_CKBOARD)
