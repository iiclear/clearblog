from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from flask_login import current_user


from extensions import db
from forms import CommentForm, AdminCommentForm
from models import Post, Category, Comment


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return render_template('blog/index.html')


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
   # 根据标签ID在数据库中查询对应文章,进行分页操作
    pass


