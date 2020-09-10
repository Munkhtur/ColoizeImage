import secrets
import os
import glob
from PIL import Image
from flask import url_for, current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static\pictures', picture_fn)

    # output_size = (125, 125)
    i = Image.open(form_picture)
    # i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn


def delete_pictures():
    image_names = os.listdir('app/static/pictures')
    results = os.listdir('app/static/result')
    if image_names:
        for name in image_names:
            os.remove('app/static/pictures/' + name)
    if results:
        for result in results:
            os.remove('app/static/result/' + result)
