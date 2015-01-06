from flask import current_app


class FlaskMacro:
    app = None

    def __init__(self,app=None):
        if app is not None:
            self.app = app
            self.init_app(app)
            

    def init_app(self,app):
        if self.app is None:
            self.app = app
        self.make_blueprint(app)

    def make_blueprint(self,app):
        from flask import Blueprint
        macro = Blueprint('macro',__name__,template_folder="templates/macros")
        self.app.register_blueprint(macro)

