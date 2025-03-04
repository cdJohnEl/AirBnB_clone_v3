#!/usr/bin/python3
"""Init file for views module"""
from flask import Blueprint

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
