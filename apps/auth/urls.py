#!/usr/bin/env python
# -*-coding:utf-8
from __future__ import absolute_import, print_function, division
from . import auth
from .views import IndexView

auth.add_url_rule("/", view_func=IndexView.as_view(r"index_view"))
