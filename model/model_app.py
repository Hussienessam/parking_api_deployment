from urllib.error import HTTPError
import urllib.request
from io import BytesIO
from PIL import Image
from flask import request, jsonify
import os
import sys

sys.path.append('/var/www/parking_finder/parking_finder/model')

import Model as Model


def find():
    input_path = '/var/www/parking_finder/parking_finder/static/image.png'
    
    if(request.is_json):
        content = request.get_json()
        url = content['url']
        capacity = content['capacity']
    else:
        url = request.form['url']
        capacity = request.form['capacity']

    imageSaved, error = saveImage(input_path, url)
    if(imageSaved):
        spots = int(capacity) - Model.model(input_path)
        return jsonify(
            spots=spots
        )
    else:
        return error


def saveImage(input_path, url):
    formats = {
        'image/jpeg': 'JPEG',
        'image/png': 'PNG',
        'image/gif': 'GIF',
        'image/jpg': 'JPG',
    }

    imageSaved = True
    error = ''

    try:
        response = urllib.request.urlopen(url)

    except HTTPError as err:
        imageSaved = False
        error = 'File not found'
        return imageSaved, error

    image_type = response.info().get('Content-Type')

    try:
        format = formats[image_type]

    except KeyError:
        imageSaved = False
        error = 'Not a supported image format'
        return imageSaved, error

    file = BytesIO(response.read())
    img = Image.open(file)
    img.save(input_path, format=format)
    return imageSaved, error

