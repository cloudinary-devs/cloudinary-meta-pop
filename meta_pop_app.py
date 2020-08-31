from flask import Flask, request, render_template
import os
import json
from retry import retry

import cloudinary
import cloudinary.api
import cloudinary.uploader

import logging
from pathlib import Path

import csv
import requests

app = Flask(__name__)

def generate_meta_string(field_name,field_required_value,metadata_tree=cloudinary.api.list_metadata_fields()):
    #first find out field in list
    for field in metadata_tree['metadata_fields']:
        if field_name.upper().strip() == field['external_id'].upper().strip():
            #when the field is found, check field type and act by it
            #string case
            if field['type'] == 'string':
                return field_name+'='+field_required_value
            #enum (single selection) case
            if field['type'] == 'enum':
                for v in field['datasource']['values']:
                    # match with option name
                    if v['value'].upper() == field_required_value.upper():
                        return field_name+'='+v['external_id']
            #integer case
            if field['type']  == 'integer':
                if isinstance(field_required_value, int):
                    return field_name+'='+field_required_value

@app.route('/foldertree', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse_tree():
    payload = request.json

    #reset metadata_string
    metadata_list = []
    metadata_string = ''

    #logic form TREE_LOGIC var is: YEAR/PRODUCT_LINE/COLOR split into a list
    tree_logic_list = tree_logic.split('/')
    if len(tree_logic_list)<1:
        return "OK"

    payload['action'] = 'incoming hook for folder tree parsing'
    print(request.json)

    #use pathlib to extrack folder parent and split it to a list
    folder_prefix_list = str(Path(payload['public_id']).parent).split('/')

    #iterate over the TREE_LOGIC list to populate the meta string
    for idx in range(len(tree_logic_list)):
        if tree_logic_list[idx] and folder_prefix_list[idx]:
            metadata_list.append(tree_logic_list[idx]+'='+folder_prefix_list[idx])
    metadata_string = '|'.join(metadata_list)
    #update the meta on the asset
    
    meta_result = cloudinary.uploader.update_metadata(metadata_string, payload['public_id'])
    meta_result['action'] = 'metadata update by folder structure'
    meta_result['metadata_string'] = metadata_string
    meta_result['metadata_list'] = metadata_list
    print(meta_result)
    return "OK"

@app.route('/manifest', methods=['POST'])
# @retry(tries=5, delay=2)
def inbound_parse_manifest():
    payload = request.json
    #reset metadata_string
    metadata_list = []
    metadata_string = ''
    metadata_tree=cloudinary.api.list_metadata_fields()
    if (payload['public_id'].split('.')[1]).lower() == 'csv':
        payload['action'] = 'incoming hook for csv parsing'
        print(request.json)
        #get the file
        with requests.Session() as s:
            download = s.get(payload['secure_url'])
            decoded_content = download.content.decode('utf-8')
            cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')

            #parse the file and make the cahnges by each line of it
            #header format should be as following
            #FILENAME,FIELD_EXT_ID1,FIELD_EXT_ID2
            #file.jpg,field_value1,field_value2

            for row in cr:
                for k, v in row.items():
                    if k != 'FILENAME':
                        metadata_item = generate_meta_string(k,v,metadata_tree)
                        # metadata_list.append(k+'='+v)
                        metadata_list.append(metadata_item)

                metadata_string = '|'.join(metadata_list)

                #search for the assets to get it's public_id
                search_results = cloudinary.Search().expression('filename='+Path(str(row['FILENAME'])).stem+'*').execute()
                # print(search_results)

                #call upon a function to update the metadata
                meta_result = cloudinary.uploader.update_metadata(metadata_string, search_results['resources'][0]['public_id'])
                meta_result['action'] = 'metadata update by csv'
                meta_result['metadata_string'] = metadata_string
                meta_result['metadata_list'] = metadata_list
                meta_result['search_results'] = search_results
                print(meta_result)
        
        return "OK"
    else:
        return "OK"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    
    cld_url = str(os.environ.get('CLOUDINARY_URL', '')) 
    filter_divider = str(os.environ.get('FILTER_DIVIDER', '__'))
    cleanup_publicid = str(os.environ.get('CLEANUP_PUBLICID', 'Yes'))
    tree_logic = str(os.environ.get('TREE_LOGIC', ''))
    logging.info("app will run on port:", port)
    app.run(host='0.0.0.0', port=port)