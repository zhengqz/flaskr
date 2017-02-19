#!/usr/bin/env python
# -*-coding:utf-8
from __future__ import absolute_import, print_function, division
from flask import Flask
from config import config
from apps.ext import db
from . import urls


def create_app(env_config="default"):
    app = Flask(__name__)
    app.config.from_object(config[env_config])
    db.init_app(app)
    urls.init_urls(app)
    return app
