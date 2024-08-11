from random import randint, choice


SIZE_N = 5
SIZE_M = 5

def check_state(char_x, char_y, enemy_x, enemy_y, char_sign_x, exit_x, exit_y):
    win_condition = char_x == exit_x and char_y == exit_y
    loss_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition:
        char_sign_x = "W"
        print(f"You Won in {turns} turns!!!")
    elif loss_condition:
        char_sign_x = "L"
        print(f"You Loss in {turns} turns!!!")
    return char_sign_x, win_condition or loss_condition


def generate_map(char_x, char_y, exit_x, exit_y,enemy_x, enemy_y,char_sign_w,char_sign_e,char_sign_x,char_sign_o, size_n=SIZE_N, size_m=SIZE_M):
    world_map =''

    for j in range (size_m):
        row = '|'
        for i in range(size_n):
            if char_x == i and char_y == j:
                row += f"{char_sign_x}|"
            elif exit_x == i and exit_y == j:
                row += f"{char_sign_o}|"
            elif enemy_x == i and enemy_y == j:
                row += f"{char_sign_e}|"
            else:
                row += " |"
        world_map += f"{row}\n"
    return world_map

def move(direction, x, y, size_n=SIZE_N, size_m=SIZE_M):
    if direction == "u" and y > 0:
        y -= 1
    elif direction == "d" and y < size_n - 1:
        y += 1
    elif direction == "l" and x > 0:
        x -= 1
    elif direction == "r" and x < size_m - 1:
        x += 1
    return x, y


char_x = randint(0, SIZE_N - 1)
char_y = randint(0, SIZE_M - 1)
char_sign_x = "X"

enemy_x = randint(0, SIZE_N - 1)
enemy_y = randint(0, SIZE_M - 1)
char_sign_e = "E"

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)
char_sign_o = "O"
char_sign_w = "W"

turns = 0

while True:

    char_sign_x, end_flag = check_state(char_x, char_y, enemy_x, enemy_y, char_sign_x, exit_x, exit_y)

    
    world_map = generate_map(char_x, char_y, exit_x, exit_y, enemy_x, enemy_y,char_sign_w,char_sign_e,char_sign_x,char_sign_o)
    print(world_map)

    if end_flag:
        break


    direction = input("Choose your next move: up / down / left / right >>> ")
    char_x, char_y = move(direction, char_x, char_y)

    enemy_direction = choice("udlr")
    enemy_x, enemy_y = move(direction, enemy_x, enemy_y)
    
    turns += 1
