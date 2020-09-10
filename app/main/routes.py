from app.main.forms import PictureForm
from app.utils import save_picture, delete_pictures
from app.image_colorization import colorize
import os
import uuid
from flask import Blueprint, render_template, url_for, redirect, session


main = Blueprint('main', __name__)


@main.route('/',  methods=['GET', 'POST'])
def home():
    image_names = os.listdir('app/static/pictures')
    results = os.listdir('app/static/result')

    form = PictureForm()
    if form.validate_on_submit():
        if form.picture.data:
            delete_pictures()
            save_picture(form.picture.data)
            return redirect(url_for('main.home'))
    return render_template('index.html', form=form, image_names=image_names, result=results)


@main.route('/colorize/<string:image>')
def user_colorize(image):
    image_name = image
    image_url = 'app/static/pictures/' + image_name
    colorize(image_url)
    return redirect(url_for('main.home'))


@main.route('/about')
def about():
    return render_template('about.html')
