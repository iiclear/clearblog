from flask import Blueprint,render_template,flash
from flask_login import login_user, logout_user, login_required, current_user
auth_bp = Blueprint('auth',__name__)

from forms import LoginForm
from models import Admin
from helper import redirect_back

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
                return redirect_back()
            flash('错误的密码或账户.', 'warning')
        else:
            flash('查无此号.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()