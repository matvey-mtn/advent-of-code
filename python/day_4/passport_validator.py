import re
from passport import Passport

passport_mappings = {
        'byr': (lambda passport_obj, val: passport_obj.set_byr(val)),
        'iyr': (lambda passport_obj, val: passport_obj.set_iyr(val)),
        'eyr': (lambda passport_obj, val: passport_obj.set_eyr(val)),
        'hgt': (lambda passport_obj, val: passport_obj.set_hgt(val)),
        'hcl': (lambda passport_obj, val: passport_obj.set_hcl(val)),
        'ecl': (lambda passport_obj, val: passport_obj.set_ecl(val)),
        'pid': (lambda passport_obj, val: passport_obj.set_pid(val)),
        'cid': (lambda passport_obj, val: passport_obj.set_cid(val))
    }


def main():
    batch = open("test_data/test_batch.txt", "r")

    passports_list = read_lines_and_consolidate_data(batch)
    parsed_passports = map_to_passports_list(passports_list)

    valid_passports = list(filter(lambda p: p.is_valid(), parsed_passports))
    valid_passports = list(filter(lambda p: is_valid_task_2(p), valid_passports))
    print(f'Valid passports count: {len(valid_passports)}')


def map_to_passports_list(passports_list):
    return list(map(lambda passport_data: to_passport(passport_data), passports_list))


def to_passport(raw_data):
    passport = Passport()
    pairs = raw_data.split()
    for pair in pairs:
        key_val = pair.split(":")
        func = passport_mappings.get(key_val[0], lambda a, b: print("Invalid Option!"))
        func(passport, key_val[1])
    return passport


def is_valid_task_2(passport: Passport):

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    return 1920 <= int(passport.birth_year) <= 2002 \
           and 2010 <= int(passport.issue_year) <= 2020 \
           and 2020 <= int(passport.expiration_year) <= 2030 \
           and re.search('^#([a-f|0-9]{6})$', passport.hair_color) \
           and re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', passport.eye_color) \
           and re.search('^\\d{9}$', passport.passport_id) \
           and (re.search('^1([5-8][0-9]|9[0-3])cm$', passport.height) or re.search('^(59|6[0-9]|7[0-6])in$', passport.height))


def read_lines_and_consolidate_data(batch):
    passports_list = []
    input_chunks = []
    for line in batch.readlines():
        if line == '\n':
            passports_list.append(" ".join(input_chunks))
            input_chunks = []
            continue

        input_chunks.append(line.replace("\n", ""))

    # flush remaining values
    if len(input_chunks) > 0:
        passports_list.append(" ".join(input_chunks))

    return passports_list

main()