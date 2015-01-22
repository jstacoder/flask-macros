from flask import current_app, get_template_attribute,Flask
from functools import partial


def get_test_app():
    app = Flask(__name__)
    macro = FlaskMacro(app)
    app.test_request_context().push()
    return app

def merge_lists(*args):
    rtn = []
    for lst in args:
        rtn += lst
    return rtn

def get_template_objs(env):
    return map(lambda x: (x.name,x.module),map(env.get_template,env.list_templates()))

def get_macro_list(itm):
    return (itm[0],[_x for _x in dir(itm[1]) if not _x.startswith('_')])

def just_macro_list(itm):
    return [_x for _x in dir(itm[1]) if not _x.startswith('_')]




def get_macros(itm):
    #partials = [partial(get_template_attribute,x[0]) for x in map(get_macro_list,get_template_objs(itm))][0]
    #return partials
    return [map(
                _partial,
                just_macro_list(
                    get_template_objs(
                        itm
                    )
                )
            ) for _partial in [partial(
                                get_template_attribute,
                                x[0]
            ) for x in map(
                        get_macro_list,
                        get_template_objs(
                                        itm
                        )
            )
            ]
    ]
    

class FlaskMacro:
    '''
        this class
    '''
    app = None

    def __init__(self,app=None):
        if app is not None:
            self.app = app
            self.init_app(app)
            
    def init_app(self,app):
        '''
            initalize the class 
        '''
        if self.app is None:
            self.app = app
        self.make_blueprint()
        self.inject_globals()

    def make_blueprint(self):
        from flask import Blueprint,current_app
        
        macros = Blueprint(__name__.split('.')[0],'macros',template_folder="templates/macros")
        if 'flask_macros' in self.app.blueprints.keys():
            self.app.blueprints.pop('flask_macros')
            self.app.register_blueprint(macros)


    def inject_globals(self):
        _macros = Macros()
        self.app.jinja_env.globals['_macros'] = _macros


class Macros:
    pass






