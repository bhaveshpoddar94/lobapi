from enum import Enum
import sys

class Fields(Enum):
    NAME = 0
    ADDRESS = 1
    CITY = 2
    STATE = 3
    COUNTRY = 4
    ZIP = 5
    MESSAGE = 6


class Parser(object):
    def parse(self, data):
        try:
            address = {
                "name": data[Fields.NAME.value],
                "address_line1": data[Fields.ADDRESS.value],
                "address_line2": "",
                "address_city": data[Fields.CITY.value],
                "address_state": data[Fields.STATE.value],
                "address_country": data[Fields.COUNTRY.value],
                "address_zip": data[Fields.ZIP.value]
            }
            if len(data[Fields.ZIP.value]) > 500:
                print("Character limit is 500 characters only")
                sys.exit(1)
        except IndexError as e:
            print("Provide name, address, city, state, country, zipcode and message")
            sys.exit(1)
        else:
            return address, ' '.join(data[1:-1]), data[Fields.MESSAGE.value]

    def readFile(self, filename):
        with open(filename, 'r') as f:
            data = f.readlines()
            return self.parse(data)

    def readStdin(self, data):
        data = [data.name, data.address, data.city,
            data.state, data.country, data.zip, data.message]
        if not all(data):
            print("Provide name, address, city, state, country, zipcode and message")
            sys.exit(1)
        return self.parse(data)
