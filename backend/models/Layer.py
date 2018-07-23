# -*- coding: utf-8 -*-
from BaseModel import *

from Type import *
from Group import *
from Category import *
from Format import *
from Attribute import *


class Layer(BaseModel):
    type_id = ForeignKeyField(Type)
    group_id = ForeignKeyField(Group)
    category_id = ForeignKeyField(Category)
    name = CharField(null=False, max_length=255)
    url = url = CharField(null=False, max_length=255)
    format_id = ForeignKeyField(Format)
    attribute_id = ForeignKeyField(Attribute)
