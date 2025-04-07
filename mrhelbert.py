import os
import random
import time

# Terminal size (you can adjust this to fit your terminal)
WIDTH = 40
HEIGHT = 10

# Initial position and direction of the "DVD" text
x = random.randint(0, WIDTH - 4)  # random starting x position
y = random.randint(0, HEIGHT - 1)  # random starting y position
dx = 1  # Horizontal movement direction
dy = 1  # Vertical movement direction

logo = "DVD"

while True:
    # Clear the terminal screen
    print('\x1b[H\x1b[2J', end='')

    # Create the empty screen
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Place the logo in its current position
    for i, char in enumerate(logo):
        screen[y][x + i] = char

    # Print the screen
    for row in screen:
        print(''.join(row))

    # Update the position
    x += dx
    y += dy

    # Check for boundary collisions and reverse direction if necessary
    if x <= 0 or x + len(logo) >= WIDTH:
        dx = -dx  # Reverse horizontal direction
    if y <= 0 or y >= HEIGHT - 1:
        dy = -dy  # Reverse vertical direction

    # Sleep for a short time to make the movement visible
    time.sleep(0.1)