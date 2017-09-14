<img src="https://travis-ci.org/pkjayk/parse-to-firebase-user-transfer.svg?branch=master">

Start environment:

. venv/bin/activate

export FLASK_DEBUG=1
export FLASK_APP=main.py

flask run


Exit venv: $ deactivate



<h1>DATA FORMAT:</h1> d
Your JSON must be an array of all mongo docs. Use --jsonArray flag when exporting from mongoDB. See https://docs.mongodb.com/v2.6/reference/program/mongoexport/#cmdoption-jsonarray.

It should look something like this:
```json
[
  {
    "_id": "123",
    "username": "jack",
    "email": "jack@jill.com",
    "first_name": "Jack",
    "last_name": "Man",
    "active_status": true,
    "_hashed_password": "1234",
    "_created_at": {
      "$date": "2017-05-07T09:30:44.587Z"
    },
    "_updated_at": {
      "$date": "2017-05-07T09:30:44.587Z"
    }
  },
  {
    "_id": "456",
    "username": "jill",
    "email": "jill@jack.com",
    "first_name": "Jill",
    "last_name": "Woman",
    "active_status": true,
    "_hashed_password": "5678",
    "_created_at": {
      "$date": "2017-08-19T03:18:13.204Z"
    },
    "_updated_at": {
      "$date": "2017-08-19T03:18:13.204Z"
    }
  }
]
```