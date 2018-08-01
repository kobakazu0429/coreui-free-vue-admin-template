# -*- coding: utf-8 -*-
import datetime

from backend.models.Category import *
from backend.flask.utils.msgs import returnResultPatch


def patch_category(id, request):
    patching_category = Category.get_by_id(id)

    patching_category.category = request.json['category']
    patching_category.updated_at = datetime.datetime.now()

    patching_category.save()

    return returnResultPatch()
