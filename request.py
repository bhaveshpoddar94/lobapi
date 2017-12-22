import lob, requests, json, sys

lob.api_key = 'test_cfc5a0154213f8ef08885fce151307bfa39'
CIVIC_API_KEY = "AIzaSyDIEfY8bvzlNspybItISV_Jq42oW6HYLH0"

class Request(object):
    def fetchRepresentative(self, from_address):
        params = {
            "address": from_address,
            "roles": "legislatorUpperBody",
            "key": CIVIC_API_KEY
        }
        response = requests.get(
            "https://www.googleapis.com/civicinfo/v2/representatives",
            params=params
        )
        response = json.loads(response.text)
        if "error" in response.keys():
            print ("Status Code: {}".format(response["error"]["code"]))
            print ("Error Message: {}".format(response["error"]["message"]))
            sys.exit(1)
        try:
            for official in response["officials"]:
                name = official.setdefault("name", "")
                payload = official.setdefault("address", [])
                if name and payload:
                    break
            else:
                print("Couldn't find senator's information")
                sys.exit(1)
            payload = payload[0]
            line2 = payload.setdefault("line2", "")
            address = {
                "name": name,
                "address_line1": payload["line1"],
                "address_line2": line2,
                "address_city": payload["city"],
                "address_state": payload["state"],
                "address_zip": payload["zip"],
            }
        except KeyError as e:
            print (str(e))
            print ("Couldn't find a senator to contact in your area")
            sys.exit(1)
        else:
            return address

    def createLetter(self, to_address, from_address, message):
        try:
            letter = lob.Letter.create(
                description="Test Lob API",
                to_address=to_address,
                from_address=from_address,
                file=open('template.html', 'rb'),
                merge_variables={
                    "message": message
                },
                color=False,
            )
        except Exception as e:
            print("Error: {}".format(str(e)))
            print("Letter could not be created")
            sys.exit(1)
        else:
            return letter
