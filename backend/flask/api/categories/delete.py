# -*- coding: utf-8 -*-
from backend.models.Category import *

from backend.flask.utils.msgs import returnResultDelete


def delete_category(id):
    deleting_category = Category.get_by_id(id)

    deleting_category.delete_instance()

    return returnResultDelete()
