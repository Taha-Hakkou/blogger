from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, expose, has_access

from . import appbuilder, db
"""
class Home(ModelView):

    #default_view = 'method1'

    @expose('/')
    @has_access
    def home(self):
        # do something with param1
        # and return to previous page or index
        page = request.args.get('page', 1, type=int)
        posts = db.session.query(Post).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template('home.html', posts=posts)

#appbuilder.add_view(Home, "home", category='Home')
appbuilder.add_link("home", href='/home', category='Home')
"""
"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template("404.html",
                        base_template=appbuilder.base_template,
                        appbuilder=appbuilder
        ),
        404
    )

@appbuilder.app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@appbuilder.app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500

db.create_all()