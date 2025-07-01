from random import choice
from time import sleep
from pynput.keyboard import Listener, Key

direction = 0 #? 0 - right, 1 - up, 2 - left, 3 - down
direction_changed_this_turn = False
run = True


#& Generates a new coordinate for an apple
def new_apple(snake, rows, cols) -> list[int]:
    #! Unavailables are the ones snake's body is in
    available_coords = [[x,y] for x in range(rows) for y in range(cols) if not [x,y] in snake]
    apple = choice(available_coords)
    return apple


#& Prints the field
def print_field(rows: int, cols: int, snake: list[list[int]], apple: list[int]):
    for y in range(cols):
        for x in range(rows):
            #! ■ for snake body, ◨/◧/⬒/⬓ for the snake head (the unfilled part looks in the direction), ● for the apple, . for empty cells
            print(f" {'■' if ([x,y] in snake[:-1]) else ("◧" if direction == 0 else '◨' if direction == 2 else '⬓' if direction == 1 else '⬒') if ([x,y] == snake[-1]) else '●' if [x,y] == apple else '.' }  ", end='')
        print('\n')


#& Changing the direction if possible (for example you can't turn right while moving left, but can if you were moving up)
def change_direction(from_d: int, to_d: int):
    if from_d-to_d==2 or from_d-to_d==-2:
        return from_d
    return to_d


#& For changing the direction on key press
def direction_on_press(key):
    #! All the global variables used
    global direction
    global direction_changed_this_turn
    global run

    #! Don't work if direction was already changed this turn (so user can't go from right to up and then left in one turn)
    if direction_changed_this_turn:
        return

    d = direction
    
    #! Checks "char" keys (a, b, 1, 2...)
    if 'char' in dir(key):
        if key.char=='w': direction = change_direction(direction, 1)
        elif key.char=='a': direction = change_direction(direction, 2)
        elif key.char=='s': direction = change_direction(direction, 3)
        elif key.char=='d': direction = change_direction(direction, 0)
        elif key.char=='q': run = False
    
    #! Checks "nonchar" keys (esc, arrows, ctrl...)
    elif key == Key.up: direction = change_direction(direction, 1)
    elif key == Key.left: direction = change_direction(direction, 2)
    elif key == Key.down: direction = change_direction(direction, 3)
    elif key == Key.right: direction = change_direction(direction, 0)
    elif key == Key.esc: run = False
    
    if d!=direction:
        direction_changed_this_turn=True


#& Main function
def main():
    global direction_changed_this_turn
    global run

    #! Map size
    rows = 15
    cols = 15

    #! The delay between frames
    frame_delay = 0.17


    #! The spawn of the snakes head
    snake_spawn_x = int(rows//3+1)
    snake_spawn_y = cols//2

    #! Initial snake location (body length - 3)
    snake = [[snake_spawn_x-2, snake_spawn_y], [snake_spawn_x-1, snake_spawn_y], [snake_spawn_x, snake_spawn_y]]

    #! First apple generation
    apple = new_apple(snake, rows, cols)

    #! Started listening to key presses
    listener = Listener(on_press=direction_on_press)
    listener.start()

    score = 0

    while run:

        print(f" SCORE: {score}\n")
        print_field(rows, cols, snake, apple)
        sleep(frame_delay)

        #! Updating in case it was True
        direction_changed_this_turn = False
        ate = False

        #! Copying the old head to put into the new position for the new frame
        new_head = snake[-1].copy()
        
        #! Movement according to direction
        if direction == 0: new_head[0]+=1 #? Right
        elif direction == 1: new_head[1]-=1 #? Up
        elif direction == 2: new_head[0]-=1 #? Left
        elif direction == 3: new_head[1]+=1 #? Down

        #! Teleporting to the opposite one if goes into the wall
        if new_head[0] == rows:
            new_head[0] = 0
        if new_head[1] == cols:
            new_head[1] = 0
        if new_head[0] == -1:
            new_head[0] = rows-1
        if new_head[1] == -1:
            new_head[1] = cols-1
        
        #! If ate an apple
        if new_head==apple:
            ate = True
            apple = new_apple(snake, rows, cols)
            score+=1

        #! Deleting the tail of the snake (if apple not eaten) 
        if not ate:
            del snake[0]

        #! Checking if head touches the body
        if new_head in snake:
            run = False
        
        #! Adding the head back (tail removed (if no apple), head added)
        snake+=[new_head]

        print('\n'*30)
    
    listener.stop()

    print('\n'*40)
    print(f"GAME OVER! Score: {score}")


if (__name__ == "__main__"):
    main()