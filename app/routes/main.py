from flask import render_template, request, Blueprint
from app.models.post import Post
from app import db
from app.models.user import User

main = Blueprint('main', __name__)

#from flask_login import current_user
@main.route("/")
@main.route("/home")
def home():
    #user_id = request.args.get('user_id')
    page = request.args.get('page', 1, type=int)
    posts = db.session.query(Post).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)#, user=db.session.query(User).get(user_id))


@main.route("/about")
def about():
    return render_template('about.html', title='About')