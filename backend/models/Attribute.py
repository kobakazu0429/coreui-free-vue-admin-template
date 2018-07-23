# -*- coding: utf-8 -*-
from BaseModel import *


class Attribute(BaseModel):
    title = CharField(null=False, max_length=255)
    url = CharField(null=False, max_length=255)
