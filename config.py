#!/usr/bin/env python
# -*-coding:utf-8
from __future__ import absolute_import, print_function, division


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    pass


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class TestingConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    DEBUG = False


config = {
    "default": DevelopConfig,
    "test": TestingConfig,
    "prod": ProductConfig,
    "dev": DevelopConfig
}
