# -*- coding: utf-8 -*-
"""Incident views."""
from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from sqlalchemy import func
from ..extensions import db

blueprint = Blueprint('{{cookiecutter.module_name}}', __name__, url_prefix='/{{cookiecutter.module_name}}', static_folder='../static')
