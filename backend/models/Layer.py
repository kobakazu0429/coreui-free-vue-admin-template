# -*- coding: utf-8 -*-
from backend.models.BaseModel import *

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *


class Layer(BaseModel):
    type_id = ForeignKeyField(Type)
    group_id = ForeignKeyField(Group)
    category_id = ForeignKeyField(Category)
    name = CharField(null=False, max_length=255)
    url = url = CharField(null=False, max_length=255)
    format_id = ForeignKeyField(Format)
    attribute_id = ForeignKeyField(Attribute)
    description = TextField()
    is_active = BooleanField(null=False, default=True)

    class Meta:
        db_table = 'layers'
