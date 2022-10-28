def player_input():
    movement = input()
    if movement == "w":
        move_player(player_pos, y_diff=-1)
    elif movement == "s":
        move_player(player_pos, y_diff=1)
    elif movement == "a":
        move_player(player_pos, x_diff=-1)
    elif movement == "d":
        move_player(player_pos, x_diff=1)
    else:
        print("illegal movement")
    pass


def move_player(prev_position, x_diff=0, y_diff=0):
    if map_array[player_pos[0] + y_diff][player_pos[1] + x_diff] != "#":
        map_array[prev_position[0]][prev_position[1]] = " "
        player_pos[1] += x_diff
        player_pos[0] += y_diff
    else:
        print("There is a wall")


def update_screen():
    map_array[player_pos[0]][player_pos[1]] = "@"
    for i in range(0, 10):
        for j in range(0, 10):
            print(map_array[i][j], " ", end="")
        print()
    pass


def update_logic():
    pass


rows = 10
columns = 10

map_array = [[" " for x in range(columns)] for y in range(rows)]
player_pos = [5, 5]


def create_map():
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == 9:
                if i == 0 and j == 4:
                    continue
                map_array[i][j] = "#"
            else:
                map_array[i][0] = "#"
                map_array[i][9] = "#"
    map_array[player_pos[0]][player_pos[1]] = "@"


def show_map():
    for i in range(0, 10):
        for j in range(0, 10):
            print(map_array[i][j], " ", end="")
        print()


if __name__ == '__main__':
    create_map()
    show_map()
    while True:
        player_input()
        update_logic()
        update_screen()
