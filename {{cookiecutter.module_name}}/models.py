# -*- coding: utf-8 -*-
"""Incident models."""
import datetime as dt

from flask import current_app
from flask_login import UserMixin
from {{cookiecutter.app_name}}.database import Column, Model, SurrogatePK, db, reference_col, relationship
from {{cookiecutter.app_name}}.extensions import bcrypt
from {{cookiecutter.app_name}}.settings import ProdConfig

import hashlib
import hmac
import base64
import urlparse
import urllib

class {{cookiecutter.module_name|title}}(SurrogatePK,Model):
    __tablename__ = '{{cookiecutter.module_name}}'
