from flask import redirect, url_for, Blueprint, request, jsonify
from flask_login import current_user, login_user, logout_user

from nmc.database import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('todo.app'))

    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user is not None and user.validate_password(password):
            login_user(user)
            return jsonify('Login success.')
        return jsonify('Invalid username or password.', 400)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify(message=_('Logout success.'))


@auth_bp.route('/register')
def register():
    # generate a random account for demo use
    username = fake.user_name()
    # make sure the generated username was not in database
    while User.query.filter_by(username=username).first() is not None:
        username = fake.user_name()
    password = fake.word()
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    item = Item(body=_('Witness something truly majestic'), author=user)
    item2 = Item(body=_('Help a complete stranger'), author=user)
    item3 = Item(body=_('Drive a motorcycle on the Great Wall of China'), author=user)
    item4 = Item(body=_('Sit on the Great Egyptian Pyramids'), done=True, author=user)
    db.session.add_all([item, item2, item3, item4])
    db.session.commit()

    return jsonify(username=username, password=password, message=_('Generate success.'))   return render_template('_login.html')
