#!/usr/bin/env python
# -*-coding:utf-8
from __future__ import absolute_import, print_function, division
from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views
