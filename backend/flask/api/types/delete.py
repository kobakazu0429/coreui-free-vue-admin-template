# -*- coding: utf-8 -*-
from backend.models.Type import *

from backend.flask.utils.msgs import returnResultDelete


def delete_type(id):
    deleting_type = Type.get_by_id(id)

    deleting_type.delete_instance()

    return returnResultDelete()
