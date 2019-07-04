from flask import Blueprint,render_template
from flask_login import logout_user,login_required,current_user,user_logged_out
auth_bp = Blueprint('auth',__name__)

from forms import LoginForm
@auth_bp.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    form = LoginForm()
    # 登陆成功进入用户首页，失败返回之前页面
    return render_template('auth/login.html',form=form)


