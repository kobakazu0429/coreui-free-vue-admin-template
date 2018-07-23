# -*- coding: utf-8 -*-
from BaseModel import *


class Format(BaseModel):
    format = CharField(null=False, max_length=255)
