# flask-tus
[tus](https://www.tus.io) server implementation for [Flask](https://flask.pocoo.org).

# Requirements
Following software stack is required to run this project:
* [python3](https://www.python.org/)
* [pip3]()
* [pipenv](https://pipenv.readthedocs.io/en/latest/) or [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

# Installation

### pipenv
```bash
$ git clone https://github.com/volesen/flask-tus.git
$ cd flask-tus

# pipenv --python $(which python3) install
$ pipenv --python /path/to/python3 install
$ pipenv --python /path/to/python3 shell

```

### virtualenviroment
```bash
$ git clone https://github.com/volesen/flask-tus.git
$ cd flask-tus

$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
### Running a demo project
```bash
$ python demo/app.py
```
Go to [127.0.0.1:5000](http://127.0.0.1:5000) and upload a file. The uploaded file will end in `demo/uploads/`

## Settings
Settings are added in app.config:
* `TUS_UPLOAD_URL` - Url of endpoint
* `TUS_UPLOAD_DIR` - Path to upload directory. Can be changed with custom models (eg. for saving in AWS S3)
* `TUS_MAX_SIZE` - Max size of a file-upload
* `TUS_TIMEDELTA` - Time allowed to complete upload

## Models
Upload states are by default saved in memory, but can be saved persistently, as in the following example:

```python
from flask import Flask
from flask_tus import FlaskTus
from flask_tus.ext import mongoengine_upload

def create_app(config):
  app = Flask(__name__)  
  app.config.from_object(config)
  flask_tus = FlaskTus(model=mongoengine)
  flask_tus.init_app()
  return app
```
