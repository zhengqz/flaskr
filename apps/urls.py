#!/usr/bin/env python
# -*-coding:utf-8
from __future__ import absolute_import, print_function, division
from apps.auth.urls import auth


def init_urls(app):
    app.register_blueprint(auth, url_prefix="/auth")
