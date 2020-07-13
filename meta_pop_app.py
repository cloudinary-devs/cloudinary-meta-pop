from flask import Flask, request, render_template
import os
import json
from retry import retry

import cloudinary
import cloudinary.api
import cloudinary.uploader

import logging

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse():
    payload = request.json
    logging.info("Now processing \n" ,json.dumps(payload))
    #add security layer to match password

    #TODO - take split logic from var
    #split original filename to metadata + just the filename
    metadata_string = payload['original_filename'].split(filter_divider)[0]

    #split the public_id to derive the original public_if
    filtered_assets_name = payload['public_id'].split(filter_divider)[1]
    
    #update resource metadata fields
    meta_result = cloudinary.uploader.update_metadata(metadata_string, payload['public_id'])
    logging.info(meta_result)

    if 'Yes' == cleanup_publicid:
        logging.info("Will cleanup the public id and set it to: ", filtered_assets_name)
        rename_results = cloudinary.uploader.rename(payload['public_id'], filtered_assets_name)
        logging.info(rename_results)
    
    
    return "OK"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    
    cld_url = str(os.environ.get('CLOUDINARY_URL', '')) 
    filter_divider = str(os.environ.get('FILTER_DIVIDER', '__'))
    cleanup_publicid = str(os.environ.get('CLEANUP_PUBLICID', 'Yes'))

    print ("app will run on port:", port)
    app.run(host='0.0.0.0', port=port)