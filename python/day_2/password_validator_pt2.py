f = open("test_input.txt", "r")


def validate(input_line):
    chunked = input_line.split()

    # get min and max
    first_and_last = chunked[0].split("-")
    first_occur = int(first_and_last[0]) - 1
    last_occur = int(first_and_last[1]) - 1

    # get char
    char = chunked[1].replace(":", "")

    # get password
    password = chunked[2]

    is_valid = (password[first_occur] == char) != (password[last_occur] == char)
    answer = "valid" if is_valid else "invalid"
    print(input_line.replace("\n", "") + " is " + answer)

    return is_valid


valid_count = 0
for line in f.readlines():
    if validate(line):
        valid_count += 1

print(valid_count)
