import json
import base64
from pprint import pprint

class transform:

	def render(self, the_json):
		return self.translate(the_json)

	def convert_to_json(self, the_json):
		return json.dumps(the_json, sort_keys=True, indent=4, separators=(',', ': '))

	def translate(self, the_json):
		# first, decode the json and create as a dictionary
		parse_json = self.decode_json(the_json)

		firebase_json = []
		value = None
		# loop through each object, make sure to grab
		# id, email, display name(username), password hash
		for user in parse_json:
			firebase_user_dict = {}
			firebase_user_dict['localId'] = user.get('_id')
			firebase_user_dict['email'] = user.get('email')
			firebase_user_dict['displayName'] = user.get('username')
			firebase_user_dict['passwordHash'] = self.base64encode(user.get('_hashed_password'))
			firebase_json.append(firebase_user_dict)

		pprint(firebase_json)
		return self.convert_to_json(firebase_json)

	def decode_json(self, the_json):
		decoded_json = ""
		try:
			decoded_json = json.loads(the_json)
		except ValueError:
			print 'Decoding JSON has failed'

		return (decoded_json)


	def base64encode(self, string):
		encoded_string = ""
		try:
			encoded_string = base64.b64encode(string)
		except TypeError:
			print 'Could not base64 encode hashed password'

		return (encoded_string)