import unittest
import transform

class TestTransformFunctions(unittest.TestCase):

    def setUp(self):
        self.convert = transform.transform(False)

    # only include a couple of fields to transform
    def test_convert_render_missing_content(self):
    	json = '[{"_id": "test"}, {"_id": "test2"}]'
    	json_object = self.convert.render(json)
    	json_expected = '[{"localId": "test"}, {"localId": "test2"}]'
        self.assertEqual(json_object, json_expected)

    # include all fields to transform
    def test_convert_complete_content(self):
    	json = '[{"_id":"123","username":"jack","email":"jack@jill.com","first_name":"Jack","last_name":"Man","active_status":true,"_hashed_password":"1234","_created_at":{"$date":"2017-05-07T09:30:44.587Z"},"_updated_at":{"$date":"2017-05-07T09:30:44.587Z"}},{"_id":"456","username":"jill","email":"jill@jack.com","first_name":"Jill","last_name":"Woman","active_status":true,"_hashed_password":"5678","_created_at":{"$date":"2017-08-19T03:18:13.204Z"},"_updated_at":{"$date":"2017-08-19T03:18:13.204Z"}}]'
    	json_object = self.convert.render(json)
    	json_expected = '[{"displayName": "jack", "email": "jack@jill.com", "localId": "123", "passwordHash": "MTIzNA=="}, {"displayName": "jill", "email": "jill@jack.com", "localId": "456", "passwordHash": "NTY3OA=="}]'
        self.assertEqual(json_object, json_expected)

    def 

if __name__ == '__main__':
    unittest.main()