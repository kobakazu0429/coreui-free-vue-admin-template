# -*- coding: utf-8 -*-
from BaseModel import *


class Group(BaseModel):
    group = CharField(null=False, max_length=255)
