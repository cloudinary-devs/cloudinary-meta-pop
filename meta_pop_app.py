from flask import Flask, request, render_template
import os
import json
from retry import retry

import cloudinary
import cloudinary.uploader

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse():
    print(json.dumps(request.data, sort_keys=True, indent=4))
    return "OK"


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 80))
  upload_preset = str(os.environ.get('UP_PRESET', 'email_uploader'))
  print ("app will run on port:", port)
  app.run(host='0.0.0.0', port=port)