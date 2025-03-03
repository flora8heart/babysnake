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
        text=f"score: {score}"
    )

    # Animation loop - player
    while True:
        # update the world
        canvas.move(player, SIZE, 0)

        # sleep
        time.sleep(DELAY)
        

if __name__ == '__main__':
    main()