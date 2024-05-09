from flask import render_template, request, Blueprint
from app import db
from app.models.user import User
from app.models.post import Post

main = Blueprint('main', __name__)


@main.route("/", strict_slashes=False)
@main.route("/home", strict_slashes=False)
def home():
    page = request.args.get('page', 1, type=int)
    posts = db.session.query(Post).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/about", strict_slashes=False)
def about():
    return render_template('about.html', title='About')