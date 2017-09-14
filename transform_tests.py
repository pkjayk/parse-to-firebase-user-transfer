import unittest
import transform

class TestTransformFunctions(unittest.TestCase):

    def setUp(self):
        self.convert = transform.transform()

    def test_convert_to_json(self):
    	# json mock object 
    	json = '[{"_id": "test"}, {"_id": "test2"}]'
    	json_object = self.convert.render(json)
    	json_expected = [ {"localId": "test"}, {"localId": "test2"} ]
        self.assertEqual(json_object, json_expected)

if __name__ == '__main__':
    unittest.main()