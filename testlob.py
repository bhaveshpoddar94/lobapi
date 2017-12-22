import argparse
from request import Request
from parse import Parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A CLI to send letters using Lob API'
    )
    parser.add_argument(
        '-f',
        action="store",
        dest="filename",
        help='Specify if reading from file.',
        default=""
    )
    parser.add_argument(
        '-n',
        action="store",
        dest="name",
        help='Name of sender'
    )
    parser.add_argument(
        '-a',
        action="store",
        dest="address",
        help='address lines 1 and 2 of sender'
    )
    parser.add_argument(
        '-ct',
        action="store",
        dest="city",
        default="",
        help='city of the sender'
    )
    parser.add_argument(
        '-s',
        action="store",
        dest="state",
        default="",
        help='state of the sender'
    )
    parser.add_argument(
        '-cn',
        action="store",
        dest="country",
        default="",
        help='country of the sender'
    )
    parser.add_argument(
        '-z',
        action="store",
        dest="zip",
        default="",
        help='zipcode of the sender'
    )
    parser.add_argument(
        '-m',
        action="store",
        dest="message",
        default="",
        help='message to the legislator'
    )
    results = parser.parse_args()
    parser = Parser()
    request = Request()
    if results.filename:
        from_address, address_string, message = parser.readFile(results.filename)
    else:
        from_address, address_string, message = parser.readStdin(results)
    to_address = request.fetchRepresentative(address_string)
    letter = request.createLetter(to_address, from_address, message)
    output = letter["url"]
    print("URL to your letter's pdf: {}".format(output))
