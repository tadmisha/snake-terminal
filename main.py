from random import choice

def new_apple(snake, rows, cols) -> list[int]:
    available_coords = [[x,y] for x in range(rows) for y in range(cols) if not [x,y] in snake]
    apple = choice(available_coords)
    return apple


def print_field(rows: int, cols: int, snake: list[list[int]], apple: list[int]):
    for y in range(cols):
        for x in range(rows):
            print(f" {'□' if ([x,y] in snake[:-1]) else "■" if ([x,y] == snake[-1]) else '●' if [x,y] == apple else '.' }  ", end='')
        print('\n')


def main():
    rows = 20
    cols = 20

    snake_spawn_x = int(rows//3+1)
    snake_spawn_y = cols//2

    snake = [[snake_spawn_x-1, snake_spawn_y], [snake_spawn_x-2, snake_spawn_y], [snake_spawn_x, snake_spawn_y]]
    direction = 0 #? 0 - right, 1 - up, 2 - left, 3 - down
    apple = new_apple(snake, rows, cols)


if (__name__ == "__main__"):
    main()