from flask import Blueprint,render_template,flash
from flask_login import login_user, logout_user, login_required, current_user
auth_bp = Blueprint('auth',__name__)

from forms import LoginForm
from models import Admin

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 登陆成功进入用户首页，失败返回之前页面
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.password==password:
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return 'Welcome back.'
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login.html', form=form)


