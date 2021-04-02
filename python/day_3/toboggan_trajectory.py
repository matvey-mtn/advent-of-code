# toboggan trajectory
map_file = open("test_input.txt", "r")


def traverse(toboggan_map, side_step, down_step, debug=False):
    number_of_trees = 0
    x_coordinate = 0

    map_size = len(toboggan_map)
    for y_coordinate in range(0, map_size, down_step):

        row = list(toboggan_map[y_coordinate].replace("\n", ""))

        if x_coordinate >= len(row):
            row = repeat_row_pattern(x_coordinate, row)

        if row[x_coordinate] == "#":
            number_of_trees += 1
            row[x_coordinate] = "X"
        else:
            row[x_coordinate] = "0"

        if debug:
            print("".join(row))

        # add step to x coordinate
        x_coordinate += side_step

    return number_of_trees


def repeat_row_pattern(x_coordinate, row_as_list):
    multiplier = int(x_coordinate / len(row_as_list))
    row_as_list += row_as_list * multiplier
    return row_as_list


def get_map_from_file(file):
    return file.readlines()


toboggan_map = get_map_from_file(map_file)
output_1 = traverse(toboggan_map, 1, 1)
print(f'output#1 = {output_1}')
output_2 = traverse(toboggan_map, 3, 1)
print(f'output#2 = {output_2}')
output_3 = traverse(toboggan_map, 5, 1)
print(f'output#3 = {output_3}')
output_4 = traverse(toboggan_map, 7, 1)
print(f'output#4 = {output_4}')
output_5 = traverse(toboggan_map, 1, 2)
print(f'output#5 = {output_5}')

print(output_1 * output_2 * output_3 * output_4 * output_5)
