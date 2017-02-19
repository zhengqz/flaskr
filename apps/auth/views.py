#!/usr/bin/env python
# -*-coding:utf-8
from __future__ import absolute_import, print_function, division
from flask.views import View
from flask import jsonify


class IndexView(View):
    def dispatch_request(self):
        context = {"test": "test 111111"}
        return jsonify(context)
