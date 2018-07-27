# -*- coding: utf-8 -*-
from backend.models.Attribute import *

from backend.flask.utils.msgs import returnResultDelete


def delete_attribute(id):
    deleting_attribute = Attribute.get_by_id(id)

    deleting_attribute.delete_instance()

    return returnResultDelete()
