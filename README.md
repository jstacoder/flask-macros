flask-macros
============

a collection of bootstrap3 jinja2 macros for use with flask apps

to use:

```python 
from flask import Flask
from flask_macros import Macro

app = Flask(__name__)
macro = Macro(app)
```
now you can import any file from flask_macros/templates/macros/*.html
ie:
```jinja2
{% import 'forms.html' as form_macros with context %}
```
or just use the jinja global _macro

either 
'''jinja2
{% set form_macros = _macros.forms %}
{% call form_macros.form_group() %}
  {{ formstuff }}
{% endcall %}
```
or 
```jinja2
{% call _macros.forms.form_group() %}
  {{ formstuff }}
{% endcall %}
```
