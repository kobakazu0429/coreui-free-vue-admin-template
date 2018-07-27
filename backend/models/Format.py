# -*- coding: utf-8 -*-
from backend.models.BaseModel import *


class Format(BaseModel):
    format = CharField(null=False, max_length=255)

    class Meta:
        db_table = 'formats'
