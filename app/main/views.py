from flask import render_template, redirect, url_for, abort, request
from ..models import User, Pitch, Comments, PitchCategory, Votes
from flask_login import login_required, current_user 
from .forms import PitchForm, CommentForm, UpdateProfile, CategoryForm
from .. import db, photos
from . import main


@main.route ('/')
def index():
    """
    Function that returns index page and data
    """
    category = PitchCategory.get_categories()
    return render_template('index.html', categories = category)

@main.route('/category/new-pitch/<int:id>', methods= ['GET', 'POST'])
@login_required
def new_pitch(id):
    """
    Function to fetch data 
    """
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)
        
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_pitch = Pitch(pitch = pitch, category_id = category.id, user_id= current_user.id)
        new_pitch.save_pitch()
        

        return redirect(url_for('.category', id= category.id))
    
    return render_template('new_pitch.html', pitch_form = form, category = category)    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))