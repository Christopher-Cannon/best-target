'''
On a map containing various military units, find the most valuable tile
to strike with a missile that has the following blast radius:

  0
 000
000000
 000
  0
'''

import random

# Define grid variables
grid_height = 20
grid_width = 20

# Define units to place in grid
unit_list = "IRLMH"

def gen_blank_map(height, width):
    return [["  " for x in range(width)] for y in range(height)]

def gen_game_map(height, width, unit_list):
    game_map = gen_blank_map(height, width)
    i, j = 0, 0

    while(i < len(game_map)):
        while(j < len(game_map[i])):
            placement_chance = random.randrange(10)
            if(placement_chance > 7):
                unit = random.randint(0, 4)
                # Formatting fluff
                game_map[i][j] = " " + unit_list[unit]
            j += 1
        i += 1
        j = 0
    return game_map

def print_map(generic_map):
    i, j = 0, 0
    while(i < len(generic_map)):
        while(j < len(generic_map[i])):
            print("{} ".format(generic_map[i][j]), end='')
            j += 1
        i += 1
        j = 0
        print()
    print()

def determine_tile_value(game_map, height, width, unit_list):
    radius_x = [-2, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
    radius_y = [0, -1, 0, 2, -2, -1, 0, 1, 2, -1, 0, 1, 2, 0]

    i, j, k, total = 0, 0, 0, 0

    num_map = gen_blank_map(height, width)

    while(i < len(game_map)):
        while(j < len(game_map[i])):
            while(k < len(radius_x)):
                try:
                    to_check = game_map[i+radius_x[k]][j+radius_y[k]]
                    # More formatting fluff needed for comparisons
                    if(to_check != "  "):
                        if(to_check == " " + unit_list[0]):
                            total += 1
                        elif(to_check == " " + unit_list[1]):
                            total += 2
                        elif(to_check == " " + unit_list[2]):
                            total += 5
                        elif(to_check == " " + unit_list[3]):
                            total += 7
                        else:
                            total += 9
                    else:
                        total += 0
                    k += 1
                except:
                    k += 1
                    continue
            # Even more formatting fluff
            if(total > 9):
                num_map[i][j] = str(total)
            else:
                num_map[i][j] = " " + str(total)
            j += 1
            k, total = 0, 0
        i += 1
        j = 0
    return num_map

def find_highest_value(num_map):
    i, j, highest, to_strike = 0, 0, 0, []
    while(i < len(num_map)):
        while(j < len(num_map[i])):
            if(int(num_map[i][j]) >= highest):
                highest = int(num_map[i][j])
                to_strike = [i, j]
            else:
                pass
            j += 1
        i += 1
        j = 0
    return [to_strike, highest]

# Create the map with units on it
the_map = gen_game_map(grid_height, grid_width, unit_list)
print_map(the_map)

# Create the map detailing tile values
num_map = determine_tile_value(the_map, grid_height, grid_width, unit_list)
print_map(num_map)

# Find the best tile to strike
lst = find_highest_value(num_map)
print("Co-ordinates to strike: X:{}, Y:{}\nValue: {}".format(lst[0][1], lst[0][0], lst[1]))
