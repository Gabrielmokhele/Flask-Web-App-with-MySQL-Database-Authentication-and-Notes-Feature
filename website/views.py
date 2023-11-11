from flask import Blueprint, render_template,request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import Note
from website import db


views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added', category='successful')

    return render_template("home.html", user=current_user)

@views.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Note.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Employee Deleted Successfully')
    return redirect(url_for('views.home'))

@views.route('/')
def Home():
    all_data = Note.query.all()
    return render_template("home.html", employees=all_data)

