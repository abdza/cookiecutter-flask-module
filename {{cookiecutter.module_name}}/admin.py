{% raw %}
# -*- coding: utf-8 -*-
"""Incident admins."""
import flask_login as login
from flask import redirect, request, url_for, flash,current_app
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.fields import QuerySelectField
from flask_admin.helpers import (get_form_data, validate_form_on_submit,get_redirect_target, flash_errors,is_form_submitted)
from flask.ext.admin import form
from flask.ext.admin.form import Select2Widget
from flask.ext.admin.helpers import get_form_data
from flask.ext.admin.base import MenuLink
from wtforms.fields import HiddenField

from wtforms.validators import DataRequired,ValidationError

{% endraw %}from {{cookiecutter.app_name}}.models import {{cookiecutter.module_name|title}}{% raw %}

import os
import os.path as op

class {% endraw %}{{cookiecutter.module_name|title }}{% raw %}ManagementAdmin(ModelView):
    """Base Model for {{cookiecutter.module_name}} management."""

    def is_accessible(self):
        """Need to make sure user is an admin to allow user management."""
        if(login.current_user.is_authenticated):
            return login.current_user.is_admin
        return False

    def inaccessible_callback(self, name, **kwargs):
        """What to do if user is not allowed to user manage."""
        return redirect(url_for('public.home', next=request.url))

class {% endraw %}{{cookiecutter.module_name|title}}Admin({{cookiecutter.module_name|title}}ManagementAdmin):{% raw %}
    pass

def add_views(admin, db):
    """Add {% endraw %}{{cookiecutter.module_name}}{% raw %} admin views into views."""
    admin.add_view({% endraw %}{{cookiecutter.module_name|title}}Admin({{cookiecutter.module_name|title}}, db.session,endpoint='accidentadmin',category='Accident Data'))
