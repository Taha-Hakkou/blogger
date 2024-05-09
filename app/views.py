from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, expose, has_access

from . import appbuilder, db
"""
class HomeView(ModelView):
    datamodel = SQLAInterface(User)

appbuilder.add_view(HomeView, "home")
#appbuilder.add_link("home", href='/home', category='Home')
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