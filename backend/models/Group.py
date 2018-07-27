# -*- coding: utf-8 -*-
from backend.models.BaseModel import *


class Group(BaseModel):
    group = CharField(null=False, max_length=255)

    class Meta:
        db_table = 'groups'
