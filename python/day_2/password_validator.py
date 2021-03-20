f = open("test_input.txt", "r")


def validate(input_line):
    chunked = input_line.split()

    # get min and max
    min_and_max = chunked[0].split("-")
    min_occur = int(min_and_max[0])
    max_occur = int(min_and_max[1])

    # get char
    char = chunked[1].replace(":", "")

    # get password
    password = chunked[2]

    # get number of occurrences
    count = password.count(char)

    return min_occur <= count <= max_occur


valid_count = 0
for line in f.readlines():
    if validate(line):
        valid_count += 1

print(valid_count)
