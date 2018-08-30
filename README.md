Hi, this is the documentation for sending a letter to a legislator,
(here Senator) using Lob's Letter API.

1. Installation:
Extract the zip file and cd to the directory.
Note: python runtime = 3.6

command: pip install -r requirements.txt

2. Instructions to run the code

2.1 Using a text file as an input
Provide each input in a separate line. Address line1 and Address line2 go in
the same line.

Format:
<name>
<address_line1> <address_line2>
<city>
<state>
<country>
<zipcode>
<message>

refer input.txt present in the directory for an actual example
run command: python testlob.py -f <relative_path_to_your_input_file>.html

2.2 Using the standard input. The help text tells you what arguments to pass
for each input.

-h, --help   show this help message and exit
-f FILENAME  Specify if reading from file.
-n NAME      Name of sender
-a ADDRESS   address lines 1 and 2 of sender
-ct CITY     city of the sender
-s STATE     state of the sender
-cn COUNTRY  country of the sender
-z ZIP       zipcode of the sender
-m MESSAGE   message to the legislator

run command: python testlob.py -n <name> -a <address_line1> <address_line2> -ct <city> -s <state> -cn <country> -z <zipcode> -m <message>

Example:
testlob.py -n "Joe Shmoe" -a "185 Berry Street Suite 170" -ct "San Francisco" -s CA -cn US -z 94107 -m "This is a test letter for Lob’s coding challenge. Thank you legislator."

Note: Put multiple word values in quotes
