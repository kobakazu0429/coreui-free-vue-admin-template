# -*- coding: utf-8 -*-
from backend.models.Format import *

from backend.flask.utils.msgs import returnResultDelete


def delete_format(id):
    deleting_format = Format.get_by_id(id)

    deleting_format.delete_instance()

    return returnResultDelete()
