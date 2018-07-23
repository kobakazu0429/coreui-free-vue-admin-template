# -*- coding: utf-8 -*-
from BaseModel import *


class Category(BaseModel):
    category = CharField(null=False, max_length=255)
