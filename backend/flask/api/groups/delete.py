# -*- coding: utf-8 -*-
from backend.models.Group import *

from backend.flask.utils.msgs import returnResultDelete


def delete_group(id):
    deleting_group = Group.get_by_id(id)

    deleting_group.delete_instance()

    return returnResultDelete()
