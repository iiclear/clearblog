from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import logout_user,login_required,current_user,user_logged_out,login_user,login_manager
auth_bp = Blueprint('auth',__name__)
from models import Admin
from forms import LoginForm


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.password == password:
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return '登录成功'
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login.html', form=form)



