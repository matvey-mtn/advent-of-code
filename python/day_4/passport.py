""" Passport class is used to represent single passport and do a basic validation on passport fields
"""


class Passport:

    def __init__(self, birth_year=None, issue_year=None, expiration_year=None, height=None, hair_color='',
                 eye_color='', passport_id=None, country_id=""):
        self.birth_year = birth_year
        self.issue_year = issue_year
        self.expiration_year = expiration_year
        self.height = height
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.passport_id = passport_id
        self.country_id = country_id

    def set_byr(self, birth_year):
        self.birth_year = birth_year

    def set_iyr(self, issue_year):
        self.issue_year = issue_year

    def set_eyr(self, expiration_year):
        self.expiration_year = expiration_year

    def set_hgt(self, height):
        self.height = height

    def set_hcl(self, hair_color):
        self.hair_color = hair_color

    def set_ecl(self, eye_color):
        self.eye_color = eye_color

    def set_pid(self, passport_id):
        self.passport_id = passport_id

    def set_cid(self, country_id):
        self.country_id = country_id

    def is_valid(self):
        """ validation from first task """

        if (self.birth_year and self.issue_year and self.expiration_year and self.height and self.hair_color
                and self.eye_color and self.passport_id):
            return True
        else:
            return False

