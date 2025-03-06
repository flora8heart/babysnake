from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # TODO: your code here
    # Player square
    player = canvas.create_rectangle(
        0,
        0,
        SIZE,
        SIZE,
        "blue"
    )

    goal = canvas.create_rectangle(
        360,
        360,
        360 + SIZE,
        360 + SIZE,
        "salmon"
    )

    score = 0
    score_text = canvas.create_text(
        10,
        380,
        anchor='w',
        font_size=20,
        text=f"score: {score}"
    )

    # Animation loop - player
    cur_direction = "right"
    while True:
        # update the world
        print(f"current direction: {cur_direction}")
        if cur_direction == "right":
            canvas.move(player, SIZE, 0)
        elif cur_direction == "left":
            canvas.move(player, - SIZE, 0)
        elif cur_direction == "up":
            canvas.move(player, 0, - SIZE)
        elif cur_direction == "down":
            canvas.move(player, 0, SIZE)

        # Set up key press
        key = canvas.get_last_key_press()

        if key == "ArrowLeft":
            print("left arrow pressed!")
            cur_direction = "left"
        elif key == "ArrowRight":
            print("righ arrow pressed!")
            cur_direction = "right"
        elif key == "ArrowUp":
            print("up arrow pressed!")
            cur_direction = "up"
        elif key == "ArrowDown":
            print("down arrow pressed!")
            cur_direction = "down"

        # sleep
        time.sleep(DELAY)

        # check canvas collision and ends the game
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        if player_x > CANVAS_WIDTH or player_x < 0:
            break
        if player_y > CANVAS_HEIGHT or player_y < 0:
            break


if __name__ == '__main__':
    main()