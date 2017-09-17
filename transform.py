import json
import base64
#import string_helper

from pprint import pprint

class transform:

	# set default vars
	pretty = False

	def __init__(self, pretty_print):
		self.pretty = pretty_print

	def render(self, the_json):
		return self.translate(the_json)

	def convert_to_json(self, the_json):
		if self.pretty:
			return json.dumps(the_json, sort_keys=True, indent=4, separators=(',', ': '))
		else:
			return json.dumps(the_json, sort_keys=True)

	def translate(self, the_json):
		# first, decode the json and create as a dictionary
		parse_json = self.decode_json(the_json)

		firebase_json = []
		# loop through each object, make sure to grab
		# id, email, display name(username), password hash
		for user in parse_json:
			firebase_user_dict = {}
			if user.get('_id'):
				firebase_user_dict['localId'] = str(user.get('_id'))
			if user.get('email'):
				firebase_user_dict['email'] = str(user.get('email'))
			if user.get('username'):
				firebase_user_dict['displayName'] = str(user.get('username'))
			if user.get('_hashed_password'):
				firebase_user_dict['passwordHash'] = self.base64encode(str(user.get('_hashed_password')))

			firebase_json.append(firebase_user_dict)

		pprint(firebase_json)
		return self.convert_to_json(firebase_json)

	def decode_json(self, the_json):
		decoded_json = ""
		try:
			decoded_json = json.loads(the_json)
		except ValueError:
			print('Decoding JSON has failed')

		return (decoded_json)


	def base64encode(self, string):
		encoded_string = ""
		try:
			encoded_string = base64.b64encode(string)
		except TypeError:
			print('Could not base64 encode hashed password')

		return (encoded_string)