# -*- coding: utf-8 -*-
from backend.models.BaseModel import *


class Category(BaseModel):
    category = CharField(null=False, max_length=255)

    class Meta:
        db_table = 'categories'
