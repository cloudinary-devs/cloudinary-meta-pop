from flask import Flask, request, render_template
import os
import json
from retry import retry

import cloudinary
import cloudinary.api
import cloudinary.uploader

import logging
from pathlib import Path

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse():
    payload = request.json
    logging.info("Now processing: \n" ,json.dumps(payload))
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

@app.route('/foldertree', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse_tree():
    payload = request.json
    logging.info("Now processing: \n" ,json.dumps(payload))
    
    #reset metadata_string
    metadata_list = []
    metadata_string = ''

    #logic form TREE_LOGIC var is: YEAR/PRODUCT_LINE/COLOR split into a list
    tree_logic_list = tree_logic.split('/')

    #use pathlib to extrack folder parent and split it to a list
    folder_prefix_list = str(Path(payload['public_id']).parent).split('/')

    #iterate over the TREE_LOGIC list to populate the meta string
    for idx in len(tree_logic_list):
        if tree_logic_list[idx] and folder_prefix_list[idx]:
            metadata_list.append(tree_logic_list[idx]+'='+folder_prefix_list[idx])
    metadata_string = '|'.join(metadata_list)
    #update the meta on the asset
    
    meta_result = cloudinary.uploader.update_metadata(metadata_string, payload['public_id'])
    logging.info(meta_result)
    
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    
    cld_url = str(os.environ.get('CLOUDINARY_URL', '')) 
    filter_divider = str(os.environ.get('FILTER_DIVIDER', '__'))
    cleanup_publicid = str(os.environ.get('CLEANUP_PUBLICID', 'Yes'))
    tree_logic = str(os.environ.get('TREE_LOGIC', ''))
    logging.info("app will run on port:", port)
    app.run(host='0.0.0.0', port=port)