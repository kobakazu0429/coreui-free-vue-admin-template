# -*- coding: utf-8 -*-
from backend.models.BaseModel import *


class Type(BaseModel):
    type = CharField(null=False, max_length=255)

    class Meta:
        db_table = 'types'
