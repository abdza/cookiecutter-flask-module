# -*- coding: utf-8 -*-
"""Incident models."""
import datetime as dt

from flask import current_app
from ..database import Column, Model, SurrogatePK, db, reference_col, relationship

class {{cookiecutter.module_name|title}}(SurrogatePK,Model):
    __tablename__ = '{{cookiecutter.module_name}}'
