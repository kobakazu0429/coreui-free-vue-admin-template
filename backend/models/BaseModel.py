# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

import datetime
from peewee import *
from backend.config import settings


db = settings.DB


class BaseModel(Model):
    created_at = DateTimeField(null=False, default=datetime.datetime.now)
    updated_at = DateTimeField(null=False, default=datetime.datetime.now)

    class Meta:
        database = db
