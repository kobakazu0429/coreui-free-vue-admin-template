# -*- coding: utf-8 -*-
from BaseModel import *


class Type(BaseModel):
    type = CharField(null=False, max_length=255)
